from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    active:bool
    

    def init(self, markId:int, active:bool, actionId:int, sourceId:int):
        self.markId = markId
        self.active = active
        
        super().__init__(actionId, sourceId)
    
    