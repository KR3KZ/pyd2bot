from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations


@dataclass
class SpouseInformationsMessage(NetworkMessage):
    spouse:FriendSpouseInformations
    
    
    def __post_init__(self):
        super().__init__()
    