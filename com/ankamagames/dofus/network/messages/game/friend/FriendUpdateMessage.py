from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendUpdateMessage(NetworkMessage):
    protocolId = 2011
    friendUpdated:FriendInformations
    
