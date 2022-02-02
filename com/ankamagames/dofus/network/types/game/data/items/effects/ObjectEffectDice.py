from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectEffectDice(ObjectEffect):
    diceNum:int
    diceSide:int
    diceConst:int
    
    
    def __post_init__(self):
        super().__init__()
    