from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


@dataclass
class IgnoredListMessage(NetworkMessage):
    ignoredList:list[IgnoredInformations]
    
    
    def __post_init__(self):
        super().__init__()
    