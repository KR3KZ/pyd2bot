from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightUnmarkCellsMessage(AbstractGameActionMessage):
    protocolId = 302
    markId:int
    
