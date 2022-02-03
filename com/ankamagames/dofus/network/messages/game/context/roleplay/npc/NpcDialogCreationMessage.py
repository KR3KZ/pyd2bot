from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogCreationMessage(NetworkMessage):
    mapId:int
    npcId:int
    

    def init(self, mapId:int, npcId:int):
        self.mapId = mapId
        self.npcId = npcId
        
        super().__init__()
    
    