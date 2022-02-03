from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect
    


class FightDispellableEffectExtendedInformations(NetworkMessage):
    actionId:int
    sourceId:int
    effect:'AbstractFightDispellableEffect'
    

    def init(self, actionId:int, sourceId:int, effect:'AbstractFightDispellableEffect'):
        self.actionId = actionId
        self.sourceId = sourceId
        self.effect = effect
        
        super().__init__()
    
    