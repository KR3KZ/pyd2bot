from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import GameFightTurnStartMessage


@dataclass
class GameFightTurnResumeMessage(GameFightTurnStartMessage):
    remainingTime:int
    
    
    def __post_init__(self):
        super().__init__()
    