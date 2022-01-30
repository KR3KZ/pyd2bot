from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations


class SpouseInformationsMessage(NetworkMessage):
    protocolId = 8493
    spouse:FriendSpouseInformations
    
    
