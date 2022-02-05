import win32com.client


class ServiceControl2V40:
    """CeVIO AIの制御機能を提供します。"""

    def __init__(self):
        self.service_control = win32com.client.Dispatch(
            "CeVIO.Talk.RemoteService2.ServiceControl2V40"
        )

    @property
    def host_version(self) -> str:
        """CeVIO AIのバージョンを取得します。"""
        return self.service_control.HostVersion

    @property
    def interface_version(self) -> str:
        """外部連携インターフェイスのバージョンを取得します。"""
        return self.service_control.InterfaceVersion

    @property
    def is_host_started(self) -> bool:
        """CeVIO AIにアクセス可能かどうかを取得します。"""
        return self.service_control.IsHostStarted

    def start_host(self, no_wait: bool) -> int:
        """
        CeVIO AIを起動します。起動済みなら何もしません。

        Parameters
        ----------
        no_wait : bool
            Trueの場合、起動のみ行います。
            アクセス可能かどうかはis_host_startedで確認します。
            Falseの場合、起動後に外部からアクセス可能になるまで制御を戻しません。

        Returns
        -------
        int
            * 0: 成功または起動済みです。
            * -1: インストール状態が不明です。
            * -2: 実行ファイルが見つかりませんでした。
            * -3: プロセスの起動に失敗しました。
            * -4: アプリケーション起動後、エラーにより終了しました。
        """
        return self.service_control.StartHost(no_wait)

    def close_host(self, mode: int) -> None:
        """
        CeVIO AIに終了を要求します。

        Parameters
        ----------
        mode : int
            処理モード。
            * 0: CeVIO AIが編集中の場合、保存や終了キャンセルが可能。
        """
        self.service_control.CloseHost(mode)
