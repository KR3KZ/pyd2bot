from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightPointsVariationMessage(AbstractGameActionMessage):
    protocolId = 7694
    targetId:int
    delta:int
    
    
