from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage


@dataclass
class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
    requestedId:int
    
    
    def __post_init__(self):
        super().__init__()
    