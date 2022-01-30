from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredListMessage(INetworkMessage):
    protocolId = 1938
    ignoredList:IgnoredInformations
    
    
