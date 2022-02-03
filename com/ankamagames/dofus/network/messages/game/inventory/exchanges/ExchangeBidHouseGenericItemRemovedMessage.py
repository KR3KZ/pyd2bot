from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseGenericItemRemovedMessage(NetworkMessage):
    objGenericId:int
    

    def init(self, objGenericId:int):
        self.objGenericId = objGenericId
        
        super().__init__()
    
    