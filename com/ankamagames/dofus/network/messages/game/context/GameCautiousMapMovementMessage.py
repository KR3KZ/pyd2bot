from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementMessage import GameMapMovementMessage


@dataclass
class GameCautiousMapMovementMessage(GameMapMovementMessage):
    
    
    def __post_init__(self):
        super().__init__()
    