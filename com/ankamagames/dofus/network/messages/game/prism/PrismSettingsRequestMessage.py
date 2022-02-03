from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismSettingsRequestMessage(NetworkMessage):
    subAreaId:int
    startDefenseTime:int
    

    def init(self, subAreaId:int, startDefenseTime:int):
        self.subAreaId = subAreaId
        self.startDefenseTime = startDefenseTime
        
        super().__init__()
    
    