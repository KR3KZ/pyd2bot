from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractPartyMessage(NetworkMessage):
    partyId:int
    

    def init(self, partyId:int):
        self.partyId = partyId
        
        super().__init__()
    
    