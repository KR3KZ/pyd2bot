from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeSetCraftRecipeMessage(NetworkMessage):
    objectGID:int
    

    def init(self, objectGID:int):
        self.objectGID = objectGID
        
        super().__init__()
    
    