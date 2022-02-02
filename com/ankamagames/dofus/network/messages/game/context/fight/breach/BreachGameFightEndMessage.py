from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import GameFightEndMessage


@dataclass
class BreachGameFightEndMessage(GameFightEndMessage):
    budget:int
    
    
    def __post_init__(self):
        super().__init__()
    