from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class GameActionFightChangeLookMessage(AbstractGameActionMessage):
    targetId:int
    entityLook:'EntityLook'
    

    def init(self, targetId:int, entityLook:'EntityLook', actionId:int, sourceId:int):
        self.targetId = targetId
        self.entityLook = entityLook
        
        super().__init__(actionId, sourceId)
    
    