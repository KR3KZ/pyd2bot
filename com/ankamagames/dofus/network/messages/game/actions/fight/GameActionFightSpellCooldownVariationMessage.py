from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


@dataclass
class GameActionFightSpellCooldownVariationMessage(AbstractGameActionMessage):
    targetId:int
    spellId:int
    value:int
    
    
    def __post_init__(self):
        super().__init__()
    