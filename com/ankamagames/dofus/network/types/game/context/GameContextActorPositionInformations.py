from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


@dataclass
class GameContextActorPositionInformations(NetworkMessage):
    contextualId:int
    disposition:EntityDispositionInformations
    
    
    def __post_init__(self):
        super().__init__()
    