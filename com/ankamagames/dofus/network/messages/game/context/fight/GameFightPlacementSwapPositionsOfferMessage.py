from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    requestId:int
    requesterId:int
    requesterCellId:int
    requestedId:int
    requestedCellId:int
    
    
    def __post_init__(self):
        super().__init__()
    