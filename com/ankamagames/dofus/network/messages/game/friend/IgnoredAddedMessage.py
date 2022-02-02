from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


@dataclass
class IgnoredAddedMessage(NetworkMessage):
    ignoreAdded:IgnoredInformations
    session:bool
    
    
    def __post_init__(self):
        super().__init__()
    