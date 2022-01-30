from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class GameActionFightChangeLookMessage(AbstractGameActionMessage):
    protocolId = 4039
    targetId:float
    entityLook:EntityLook
    
