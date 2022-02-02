from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


@dataclass
class FriendsListMessage(NetworkMessage):
    friendsList:list[FriendInformations]
    
    
    def __post_init__(self):
        super().__init__()
    