from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagRoomPreviewInformation(NetworkMessage):
    roomId:int
    themeId:int
    

    def init(self, roomId:int, themeId:int):
        self.roomId = roomId
        self.themeId = themeId
        
        super().__init__()
    
    