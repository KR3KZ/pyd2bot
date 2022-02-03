from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
    


class FriendsListMessage(NetworkMessage):
    friendsList:list['FriendInformations']
    

    def init(self, friendsList:list['FriendInformations']):
        self.friendsList = friendsList
        
        super().__init__()
    
    