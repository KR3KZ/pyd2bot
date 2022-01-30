from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReflectDamagesMessage(AbstractGameActionMessage):
    protocolId = 140
    targetId:int
    
