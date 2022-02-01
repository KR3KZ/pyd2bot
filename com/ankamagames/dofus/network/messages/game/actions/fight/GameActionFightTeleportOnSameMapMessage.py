from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTeleportOnSameMapMessage(AbstractGameActionMessage):
    targetId:int
    cellId:int
    
    
