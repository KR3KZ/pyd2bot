from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightCarryCharacterMessage(AbstractGameActionMessage):
    protocolId = 5643
    targetId:float
    cellId:int
    
