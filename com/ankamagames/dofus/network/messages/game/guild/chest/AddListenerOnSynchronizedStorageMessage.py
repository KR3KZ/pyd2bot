from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AddListenerOnSynchronizedStorageMessage(NetworkMessage):
    player: str

    def init(self, player_: str):
        self.player = player_

        super().__init__()
