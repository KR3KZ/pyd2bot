from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightReflectSpellMessage(AbstractGameActionMessage):
    protocolId = 8272
    targetId:int
    
    
