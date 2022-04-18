from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHousePriceMessage(NetworkMessage):
    genId: int

    def init(self, genId_: int):
        self.genId = genId_

        super().__init__()
