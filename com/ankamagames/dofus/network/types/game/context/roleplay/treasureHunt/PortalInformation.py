from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PortalInformation(NetworkMessage):
    portalId:int
    areaId:int
    

    def init(self, portalId:int, areaId:int):
        self.portalId = portalId
        self.areaId = areaId
        
        super().__init__()
    
    