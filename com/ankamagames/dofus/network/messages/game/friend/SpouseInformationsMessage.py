from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendSpouseInformations import FriendSpouseInformations


class SpouseInformationsMessage(NetworkMessage):
    spouse:FriendSpouseInformations
    
    
