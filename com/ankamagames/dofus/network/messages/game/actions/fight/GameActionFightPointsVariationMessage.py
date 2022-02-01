from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightPointsVariationMessage(AbstractGameActionMessage):
    targetId:int
    delta:int
    
    
