from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
    


class BreachBonusMessage(NetworkMessage):
    bonus:'ObjectEffectInteger'
    

    def init(self, bonus:'ObjectEffectInteger'):
        self.bonus = bonus
        
        super().__init__()
    
    