from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    protocolId = 8860
    targetId:float
    destinationCellId:int
    critical:int
    
