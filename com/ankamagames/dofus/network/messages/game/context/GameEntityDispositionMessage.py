from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations


@dataclass
class GameEntityDispositionMessage(NetworkMessage):
    disposition:IdentifiedEntityDispositionInformations
    
    
    def __post_init__(self):
        super().__init__()
    