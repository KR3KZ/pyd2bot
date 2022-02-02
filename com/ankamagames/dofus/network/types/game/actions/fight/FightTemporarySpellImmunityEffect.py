from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


@dataclass
class FightTemporarySpellImmunityEffect(AbstractFightDispellableEffect):
    immuneSpellId:int
    
    
    def __post_init__(self):
        super().__init__()
    