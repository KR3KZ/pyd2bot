from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    targetId:int
    destinationCellId:int
    critical:int
    silentCast:bool
    verboseCast:bool
    

    def init(self, targetId:int, destinationCellId:int, critical:int, actionId:int, sourceId:int):
        self.targetId = targetId
        self.destinationCellId = destinationCellId
        self.critical = critical
        
        super().__init__(actionId, sourceId)
    
    