from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredAddedMessage(NetworkMessage):
    protocolId = 6480
    ignoreAdded:IgnoredInformations
    session:bool
    
