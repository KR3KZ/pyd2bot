from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations


@dataclass
class FinishMoveListMessage(NetworkMessage):
    finishMoves:list[FinishMoveInformations]
    
    
    def __post_init__(self):
        super().__init__()
    