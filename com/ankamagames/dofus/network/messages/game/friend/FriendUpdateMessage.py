from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendUpdateMessage(NetworkMessage):
    friendUpdated:FriendInformations
    
    
