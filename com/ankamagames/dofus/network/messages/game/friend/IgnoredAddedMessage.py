from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredAddedMessage(INetworkMessage):
    protocolId = 6480
    ignoreAdded:IgnoredInformations
    session:bool
    
    
