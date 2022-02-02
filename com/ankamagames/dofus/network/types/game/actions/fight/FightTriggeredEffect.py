from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


@dataclass
class FightTriggeredEffect(AbstractFightDispellableEffect):
    param1:int
    param2:int
    param3:int
    delay:int
    
    
    def __post_init__(self):
        super().__init__()
    