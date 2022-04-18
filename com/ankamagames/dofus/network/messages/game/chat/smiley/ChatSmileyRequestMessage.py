from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatSmileyRequestMessage(NetworkMessage):
    smileyId: int

    def init(self, smileyId_: int):
        self.smileyId = smileyId_

        super().__init__()
