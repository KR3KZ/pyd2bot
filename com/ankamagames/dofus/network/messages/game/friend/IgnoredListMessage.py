from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredListMessage(NetworkMessage):
    protocolId = 1938
    ignoredList:IgnoredInformations
    
