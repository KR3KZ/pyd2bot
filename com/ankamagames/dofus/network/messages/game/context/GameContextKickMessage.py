from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextKickMessage(NetworkMessage):
    targetId: int

    def init(self, targetId_: int):
        self.targetId = targetId_

        super().__init__()
