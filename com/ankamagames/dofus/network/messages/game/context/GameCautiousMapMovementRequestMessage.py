from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementRequestMessage import GameMapMovementRequestMessage


@dataclass
class GameCautiousMapMovementRequestMessage(GameMapMovementRequestMessage):
    
    
    def __post_init__(self):
        super().__init__()
    