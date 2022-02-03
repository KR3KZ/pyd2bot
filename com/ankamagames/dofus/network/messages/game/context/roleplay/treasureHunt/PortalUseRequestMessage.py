from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PortalUseRequestMessage(NetworkMessage):
    portalId:int
    

    def init(self, portalId:int):
        self.portalId = portalId
        
        super().__init__()
    
    