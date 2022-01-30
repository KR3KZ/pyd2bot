from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionFightTargetedAbilityMessage(AbstractGameActionMessage):
    protocolId = 8860
    targetId:int
    destinationCellId:int
    critical:int
    silentCast:bool
    verboseCast:bool
    
    
