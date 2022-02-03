from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightStealKamaMessage(AbstractGameActionMessage):
    targetId:int
    amount:int
    

    def init(self, targetId:int, amount:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.amount = amount
        
        super().__init__(actionId, sourceId)
    
    