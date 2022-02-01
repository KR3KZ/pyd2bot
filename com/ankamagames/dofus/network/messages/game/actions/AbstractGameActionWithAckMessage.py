from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class AbstractGameActionWithAckMessage(AbstractGameActionMessage):
    waitAckId:int
    
    
