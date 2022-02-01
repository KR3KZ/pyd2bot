from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTackledMessage(AbstractGameActionMessage):
    tacklersIds:list[int]
    
    
