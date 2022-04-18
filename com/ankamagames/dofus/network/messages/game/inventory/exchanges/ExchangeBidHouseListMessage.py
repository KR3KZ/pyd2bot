from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseListMessage(NetworkMessage):
    id: int
    follow: bool

    def init(self, id_: int, follow_: bool):
        self.id = id_
        self.follow = follow_

        super().__init__()
