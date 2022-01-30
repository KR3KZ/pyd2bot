from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightInvisibilityMessage(AbstractGameActionMessage):
    protocolId = 7441
    targetId:float
    state:int
    
