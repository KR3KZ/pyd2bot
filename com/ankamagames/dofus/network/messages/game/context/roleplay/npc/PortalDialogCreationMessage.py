from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcDialogCreationMessage import NpcDialogCreationMessage


class PortalDialogCreationMessage(NpcDialogCreationMessage):
    type:int
    

    def init(self, type:int, mapId:int, npcId:int):
        self.type = type
        
        super().__init__(mapId, npcId)
    
    