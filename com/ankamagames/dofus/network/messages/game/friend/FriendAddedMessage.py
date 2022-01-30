from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendAddedMessage(INetworkMessage):
    protocolId = 9476
    friendAdded:FriendInformations
    
    
