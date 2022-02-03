from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListRemovedMessage(NetworkMessage):
    itemUID:int
    objectGID:int
    objectType:int
    

    def init(self, itemUID:int, objectGID:int, objectType:int):
        self.itemUID = itemUID
        self.objectGID = objectGID
        self.objectType = objectType
        
        super().__init__()
    
    