from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTeleportOnSameMapMessage(AbstractGameActionMessage):
    protocolId = 7589
    targetId:int
    cellId:int
    
    
