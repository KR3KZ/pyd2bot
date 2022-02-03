from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
    


class GameActionFightDispellableEffectMessage(AbstractGameActionMessage):
    effect:'AbstractFightDispellableEffect'
    

    def init(self, effect:'AbstractFightDispellableEffect', actionId:int, sourceId:int):
        self.effect = effect
        
        super().__init__(actionId, sourceId)
    
    