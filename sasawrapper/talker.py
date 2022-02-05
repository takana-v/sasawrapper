import win32com.client


class Talker2V40:
    """トーク機能を提供します。"""

    def __init__(self):
        self.talker2 = win32com.client.Dispatch("CeVIO.Talk.RemoteService2.Talker2V40")

    @property
    def volume(self) -> int:
        """音の大きさ（0～100）を取得または設定します。"""
        return self.talker2.Volume

    @volume.setter
    def volume(self, val: int) -> None:
        self.talker2.Volume = val

    @property
    def speed(self) -> int:
        """話す速さ（0～100）を取得または設定します。"""
        return self.talker2.Speed

    @speed.setter
    def speed(self, val: int) -> None:
        self.talker2.Speed = val

    @property
    def tone(self) -> int:
        """音の高さ（0～100）を取得または設定します。"""
        return self.talker2.Tone

    @tone.setter
    def tone(self, val: int) -> None:
        self.talker2.Tone = val

    @property
    def tone_scale(self) -> int:
        """抑揚（0～100）を取得または設定します。"""
        return self.talker2.ToneScale

    @tone_scale.setter
    def tone_scale(self, val: int) -> None:
        self.talker2.ToneScale = val

    @property
    def alpha(self) -> int:
        """声質（0～100）を取得または設定します。"""
        return self.talker2.Alpha

    @alpha.setter
    def alpha(self, val: int) -> None:
        self.talker2.Alpha = val

    @property
    def components(self) -> "TalkerComponentArray2":
        """現在のキャストの感情パラメータマップを取得します。"""
        return self.talker2.Components

    @property
    def cast(self) -> str:
        """キャストを取得または設定します。"""
        return self.talker2.Cast

    @cast.setter
    def cast(self, val: str) -> None:
        self.talker2.Cast = val

    @property
    def available_casts(self) -> "StringArray2":
        """利用可能なキャスト名を取得します。"""
        return self.talker2.AvailableCasts

    def speak(self, text: str) -> "SpeakingState2":
        """
        指定したセリフの再生を開始します。

        Parameters
        ----------
        text : str
            読み上げるセリフ

        Returns
        -------
        SpeakingState2
            再生状態を表すオブジェクト
        """
        return self.talker2.Speak(text)

    def stop(self) -> bool:
        """
        再生を停止します。

        Returns
        -------
        bool
            停止に成功したかどうか
        """
        return self.talker2.Stop()

    def get_text_duration(self, text: str) -> float:
        """
        指定したセリフの長さを取得します。

        Parameters
        ----------
        text : str
            長さを取得するセリフ。

        Returns
        -------
        float
            セリフの長さ。単位は秒です。
        """
        return self.talker2.GetTextDuration(text)

    def get_phonemes(self, text: str) -> "PhonemeDataArray2":
        """
        指定したデータの音素単位のデータを取得します。

        Parameters
        ----------
        text : str
            データを取得するセリフ。

        Returns
        -------
        PhonemeDataArray2
            音素データの配列を表すオブジェクト。
        """
        return self.talker2.GetPhonemes(text)

    def output_wave_to_file(self, text: str, path: str) -> bool:
        """
        指定したセリフをWAVファイルとして出力します。

        Parameters
        ----------
        text : str
            出力するセリフ。
        path : str
            WAVファイルの出力先パス。

        Returns
        -------
        bool
            出力に成功したかどうか

        Notes
        -----
        出力形式はサンプリングレート48kHz、ビットレート16bit、モノラルです。
        """
        return self.talker2.OutputWaveToFile(text, path)


class TalkerComponentArray2:
    """感情パラメータマップを表すオブジェクト。"""

    def __init__(self, com_obj: win32com.client.CDispatch) -> None:
        """
        Parameters
        ----------
        com_obj : win32com.client.CDispatch
            感情パラメータマップを表すCOMオブジェクト。
        """
        self.talker_component_array2 = com_obj

    @property
    def length(self) -> int:
        """配列の要素数を取得します。"""
        return self.talker_component_array2.Length

    def at(self, index: int) -> "TalkerComponent2":
        """
        指定したインデックスの要素を取得します。

        Parameters
        ----------
        index : int
            取得する要素のインデックス。

        Returns
        -------
        TalkerComponent2
            感情パラメータの単位オブジェクト。
        """
        return TalkerComponent2(self.talker_component_array2.At(index))

    def by_name(self, name: str) -> "TalkerComponent2":
        """
        指定した名前の要素を取得します。

        Parameters
        ----------
        name : str
            取得する要素の名前。

        Returns
        -------
        TalkerComponent2
            感情パラメータの単位オブジェクト。
        """

    def duplicate(self) -> "TalkerComponentArray2":
        """
        配列を複製します。

        Returns
        -------
        TalkerComponentArray2
            複製された配列。
        """
        return TalkerComponentArray2(self.talker_component_array2.Duplicate())


class TalkerComponent2:
    """感情パラメータの単位オブジェクト。"""

    def __init__(self, com_obj: win32com.client.CDispatch) -> None:
        """
        Parameters
        ----------
        com_obj : win32com.client.CDispatch
            感情パラメータの単位を表すCOMオブジェクト。
        """
        self.talker_component2 = com_obj

    @property
    def id(self) -> str:
        """感情の識別子を取得します。"""
        return self.talker_component2.Id

    @property
    def name(self) -> str:
        """感情の名前を取得します。"""
        return self.talker_component2.Name

    @property
    def value(self) -> int:
        """感情の値（0～100）を取得または設定します。"""
        return self.talker_component2.Value

    @value.setter
    def value(self, val: int) -> None:
        self.talker_component2.Value = val


class SpeakingState2:
    """再生状態を表すオブジェクト"""

    def __init__(self, com_obj: win32com.client.CDispatch):
        """
        Parameters
        ----------
        com_obj : win32com.client.CDispatch
            再生状態を表すCOMオブジェクト。
        """
        self.speaking_state2 = com_obj

    @property
    def is_completed(self) -> bool:
        """再生が完了したかどうかを取得します。"""
        return self.speaking_state2.IsCompleted

    @property
    def is_succeeded(self) -> bool:
        """再生が成功したかどうかを取得します。"""
        return self.speaking_state2.IsSucceeded

    def wait(self) -> None:
        """
        再生終了を待ちます。
        """
        self.speaking_state2.Wait()

    def wait_2(self, timeout: float) -> None:
        """
        再生終了を待ちます。

        Parameters
        ----------
        timeout : float
            最大待機時間。単位は秒です。
            0未満にすると無制限に待機します。
        """
        self.speaking_state2.Wait_2(timeout)


class PhonemeDataArray2:
    """音素データの配列を表すオブジェクト。"""

    def __init__(self, com_obj: win32com.client.CDispatch):
        """
        Parameters
        ----------
        com_obj : win32com.client.CDispatch
            音素データの配列を表すCOMオブジェクト。
        """
        self.phoneme_data_array2 = com_obj

    @property
    def length(self) -> int:
        """配列の要素数を取得します。"""
        return self.phoneme_data_array2.Length

    def at(self, index: int) -> "PhonemeData2":
        """
        指定したインデックスの要素を取得します。

        Parameters
        ----------
        index : int
            取得する要素のインデックス

        Returns
        -------
        PhonemeData2
            音素データの単位オブジェクト。
        """
        return self.phoneme_data_array2.At(index)

    def duplicate(self) -> "PhonemeDataArray2":
        """
        配列を複製します。

        Returns
        -------
        PhonemeDataArray2
            複製された配列。
        """
        return self.phoneme_data_array2.Duplicate()


class PhonemeData2:
    """音素データの単位オブジェクト。"""

    def __init__(self, com_obj: win32com.client.CDispatch):
        """
        Parameters
        ----------
        com_obj : win32com.client.CDispatch
            音素データの単位を表すCOMオブジェクト。
        """
        self.phoneme_data2 = com_obj

    @property
    def phoneme(self) -> str:
        """音素を取得します。"""
        return self.phoneme_data2.Phoneme

    @property
    def start_time(self) -> float:
        """開始時間を取得します。単位は秒です。"""
        return self.phoneme_data2.StartTime

    @property
    def end_time(self) -> float:
        """終了時間を取得します。単位は秒です。"""
        return self.phoneme_data2.EndTime


class StringArray2:
    """文字列の配列を表すオブジェクト。"""

    def __init__(self, com_obj: win32com.client.CDispatch):
        """
        Parameters
        ----------
        com_obj : win32com.client.CDispatch
            音素データの配列を表すCOMオブジェクト。
        """
        self.string_array2 = com_obj

    @property
    def length(self) -> int:
        """配列の要素数を取得します。"""
        return self.string_array2.Length

    def at(self, index: int) -> str:
        """
        指定したインデックスの要素を取得します。

        Parameters
        ----------
        index : int
            取得する要素のインデックス

        Returns
        -------
        str
            指定したインデックスの要素
        """
        return self.string_array2.At(index)

    def duplicate(self) -> "StringArray2":
        """
        配列を複製します。

        Returns
        -------
        StringArray2
            複製された配列。
        """
        return self.string_array2.Duplicate()
