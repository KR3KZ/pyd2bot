from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReflectSpellMessage(AbstractGameActionMessage):
    targetId:int
    

    def init(self, targetId:int, actionId:int, sourceId:int):
        self.targetId = targetId
        
        super().__init__(actionId, sourceId)
    
    