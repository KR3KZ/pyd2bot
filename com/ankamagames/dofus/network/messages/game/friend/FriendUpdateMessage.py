from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations


class FriendUpdateMessage(INetworkMessage):
    protocolId = 2011
    friendUpdated:FriendInformations
    
    
