from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightDropCharacterMessage(AbstractGameActionMessage):
    protocolId = 2160
    targetId:float
    cellId:int
    
