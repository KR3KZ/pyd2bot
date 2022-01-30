from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendsListMessage(NetworkMessage):
    protocolId = 6666
    friendsList:FriendInformations
    
