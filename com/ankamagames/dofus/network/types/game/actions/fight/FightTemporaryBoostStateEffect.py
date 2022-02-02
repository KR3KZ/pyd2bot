from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import FightTemporaryBoostEffect


@dataclass
class FightTemporaryBoostStateEffect(FightTemporaryBoostEffect):
    stateId:int
    
    
    def __post_init__(self):
        super().__init__()
    