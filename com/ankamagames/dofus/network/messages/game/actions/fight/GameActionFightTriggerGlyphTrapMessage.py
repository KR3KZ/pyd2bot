from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


@dataclass
class GameActionFightTriggerGlyphTrapMessage(AbstractGameActionMessage):
    markId:int
    markImpactCell:int
    triggeringCharacterId:int
    triggeredSpellId:int
    
    
    def __post_init__(self):
        super().__init__()
    