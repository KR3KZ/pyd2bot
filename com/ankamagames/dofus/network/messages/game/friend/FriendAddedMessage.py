from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendAddedMessage(NetworkMessage):
    protocolId = 9476
    friendAdded:FriendInformations
    
    
