from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations


class SpouseInformationsMessage(INetworkMessage):
    protocolId = 8493
    spouse:FriendSpouseInformations
    
    
