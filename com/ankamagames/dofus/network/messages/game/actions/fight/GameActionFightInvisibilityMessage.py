from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightInvisibilityMessage(AbstractGameActionMessage):
    targetId:int
    state:int
    
    
