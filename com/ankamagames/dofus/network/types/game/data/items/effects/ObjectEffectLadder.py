from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectCreature import ObjectEffectCreature


@dataclass
class ObjectEffectLadder(ObjectEffectCreature):
    monsterCount:int
    
    
    def __post_init__(self):
        super().__init__()
    