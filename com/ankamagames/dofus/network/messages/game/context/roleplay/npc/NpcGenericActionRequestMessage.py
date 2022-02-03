from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcGenericActionRequestMessage(NetworkMessage):
    npcId:int
    npcActionId:int
    npcMapId:int
    

    def init(self, npcId:int, npcActionId:int, npcMapId:int):
        self.npcId = npcId
        self.npcActionId = npcActionId
        self.npcMapId = npcMapId
        
        super().__init__()
    
    