from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement


@dataclass
class InteractiveElementWithAgeBonus(InteractiveElement):
    ageBonus:int
    
    
    def __post_init__(self):
        super().__init__()
    