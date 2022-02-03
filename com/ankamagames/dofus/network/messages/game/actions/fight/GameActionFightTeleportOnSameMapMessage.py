from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTeleportOnSameMapMessage(AbstractGameActionMessage):
    targetId:int
    cellId:int
    

    def init(self, targetId:int, cellId:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.cellId = cellId
        
        super().__init__(actionId, sourceId)
    
    