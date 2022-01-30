from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendsListMessage(INetworkMessage):
    protocolId = 6666
    friendsList:FriendInformations
    
    
