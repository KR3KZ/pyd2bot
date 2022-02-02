from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class GameActionFightChangeLookMessage(AbstractGameActionMessage):
    targetId:int
    entityLook:EntityLook
    
    
    def __post_init__(self):
        super().__init__()
    