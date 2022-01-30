from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDispellMessage(AbstractGameActionMessage):
    protocolId = 4560
    targetId:float
    verboseCast:bool
    
