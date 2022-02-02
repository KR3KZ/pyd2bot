from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


@dataclass
class BreachBonusMessage(NetworkMessage):
    bonus:ObjectEffectInteger
    
    
    def __post_init__(self):
        super().__init__()
    