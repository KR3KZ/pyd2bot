from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
    protocolId = 3549
    waitAckId:int
    
