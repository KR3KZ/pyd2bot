from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDispellMessage(AbstractGameActionMessage):
    targetId:int
    verboseCast:bool
    
    
