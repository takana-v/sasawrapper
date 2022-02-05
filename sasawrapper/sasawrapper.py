from typing import Dict, List, Optional

from .service_control import ServiceControl2V40
from .talker import Talker2V40

_service_control = ServiceControl2V40()
_talker = Talker2V40()


def _check_cevioai_status():
    if not _service_control.is_host_started:
        if not start_cevioai():
            raise RuntimeError("CeVIO AIへの起動、接続に失敗しました。")


def _set_values(
    volume: int,
    speed: int,
    tone: int,
    tone_scale: int,
    alpha: int,
    cast: Optional[str],
    emotion: Optional[Dict[str, int]],
):
    _check_cevioai_status()
    _cast_info = cast_info()
    if cast is None:
        cast = list(_cast_info.keys())[0]
    if cast not in _cast_info:
        raise RuntimeError("指定されたキャストがみつかりません。")
    for val in (volume, speed, tone, tone_scale, alpha):
        if not isinstance(val, int) or not 0 <= val <= 100:
            raise ValueError("無効な値です。0から100までの整数にしてください。")
    _talker.cast = cast
    component = _talker.components
    if emotion is None:
        emotion = {component.at(0).name: 100}
    for i in range(component.length):
        if component.at(i).name in emotion.keys():
            component.at(i).value = emotion[component.at(i).name]
        else:
            component.at(i).value = 0
    _talker.volume = volume
    _talker.speed = speed
    _talker.tone = tone
    _talker.tone_scale = tone_scale
    _talker.alpha = alpha


def start_cevioai(block=True) -> bool:
    """
    CeVIO AIを起動します。

    Parameters
    ----------
    block : bool, default=True
        起動が完了するまでブロック（待機）するかどうか

    Returns
    -------
    bool
        起動に成功したかどうか
    """
    return _service_control.start_host(not block) == 0


def close_cevioai():
    """
    CeVIO AIに終了を要求します。

    Notes
    -----
    CeVIO AIが編集中の場合、保存や終了キャンセルが可能です。
    """
    _check_cevioai_status()
    _service_control.close_host(0)


def cevioai_version() -> str:
    """
    CeVIO AIのバージョンを取得します。

    Returns
    -------
    str
        CeVIO AIのバージョン
    """
    _check_cevioai_status()
    return _service_control.host_version


def interface_version() -> str:
    """
    CeVIO AI 外部連携インターフェイスのバージョンを取得します。

    Returns
    -------
    str
        CeVIO AI 外部連携インターフェイスのバージョン
    """
    _check_cevioai_status()
    return _service_control.interface_version


def cast_info() -> Dict[str, List[str]]:
    """
    キャストの情報を取得します。

    Returns
    -------
    cast_info : dict
        キーがキャスト名、値が感情のリストである辞書です。

    Examples
    --------
    >>> get_cast_info()
    {'さとうささら': ['元気', '普通', '怒り', '哀しみ']}
    """
    _check_cevioai_status()
    casts = _talker.available_casts
    casts_info = {}
    for i in range(casts.length):
        casts_info[casts.at(i)] = []
    for c in casts_info:
        _talker.cast = c
        components = _talker.components
        for i in range(components.length):
            casts_info[c].append(components.at(i).name)
    return casts_info


def speak(
    text: str,
    volume: int = 50,
    speed: int = 50,
    tone: int = 50,
    tone_scale: int = 50,
    alpha: int = 50,
    cast: Optional[str] = None,
    emotion: Optional[Dict[str, int]] = None,
    block: bool = True,
):
    """
    指定したテキストの読み上げを行います。

    Parameters
    ----------
    text : str
        読み上げるテキスト（セリフ）
    volume : int, optional, default=50
        音の大きさ（0～100）
    speed : int, optional, default=50
        話す速さ（0～100）
    tone : int, optional, default=50
        音の高さ（0～100）
    tone_scale : int, optional, default=50
        抑揚（0～100）
    alpha : int, optional, default=50
        声質（0～100）
    cast : str, optional, default=None
        読み上げるキャスト
        Noneの場合、available_castsの先頭が選ばれます。
    emotion : dict, optional, default=None
        キーが感情名、値が感情の値である辞書
        指定されていない感情は0にセットされます。
    block : bool, default=True
        再生が終わるまで動作をブロックするかどうか
    """
    _check_cevioai_status()
    _set_values(
        volume=volume,
        speed=speed,
        tone=tone,
        tone_scale=tone_scale,
        alpha=alpha,
        cast=cast,
        emotion=emotion,
    )
    speaking_state = _talker.speak(text)
    if block:
        try:
            speaking_state.wait()
        except TypeError:
            pass


def output_to_wav(
    text: str,
    path: str,
    volume: int = 50,
    speed: int = 50,
    tone: int = 50,
    tone_scale: int = 50,
    alpha: int = 50,
    cast: Optional[str] = None,
    emotion: Optional[Dict[str, int]] = None,
) -> bool:
    """
    指定したパスにWAVファイルとして保存します。

    Parameters
    ----------
    text : str
        読み上げるテキスト（セリフ）
    path : str
        WAVファイルの保存先のパス
    volume : int, optional, default=50
        音の大きさ（0～100）
    speed : int, optional, default=50
        話す速さ（0～100）
    tone : int, optional, default=50
        音の高さ（0～100）
    tone_scale : int, optional, default=50
        抑揚（0～100）
    alpha : int, optional, default=50
        声質（0～100）
    cast : str, optional, default=None
        読み上げるキャスト
        Noneの場合、available_castsの先頭が選ばれます。
    emotion : dict, optional, default=None
        キーが感情名、値が感情の値である辞書
        指定されていない感情は0にセットされます。

    Returns
    -------
    bool
        出力に成功したかどうか
    """
    _check_cevioai_status()
    _set_values(
        volume=volume,
        speed=speed,
        tone=tone,
        tone_scale=tone_scale,
        alpha=alpha,
        cast=cast,
        emotion=emotion,
    )
    return _talker.output_wave_to_file(text, path)


def text_duration(
    text: str,
    volume: int = 50,
    speed: int = 50,
    tone: int = 50,
    tone_scale: int = 50,
    alpha: int = 50,
    cast: Optional[str] = None,
    emotion: Optional[Dict[str, int]] = None,
) -> float:
    """
    指定したテキストの長さを取得します。

    Parameters
    ----------
    text : str
        読み上げるテキスト（セリフ）
    volume : int, optional, default=50
        音の大きさ（0～100）
    speed : int, optional, default=50
        話す速さ（0～100）
    tone : int, optional, default=50
        音の高さ（0～100）
    tone_scale : int, optional, default=50
        抑揚（0～100）
    alpha : int, optional, default=50
        声質（0～100）
    cast : str, optional, default=None
        読み上げるキャスト
        Noneの場合、available_castsの先頭が選ばれます。
    emotion : dict, optional, default=None
        キーが感情名、値が感情の値である辞書
        指定されていない感情は0にセットされます。

    Returns
    -------
    float
        テキストの長さ
    """
    _check_cevioai_status()
    _set_values(
        volume=volume,
        speed=speed,
        tone=tone,
        tone_scale=tone_scale,
        alpha=alpha,
        cast=cast,
        emotion=emotion,
    )
    return _talker.get_text_duration(text)
