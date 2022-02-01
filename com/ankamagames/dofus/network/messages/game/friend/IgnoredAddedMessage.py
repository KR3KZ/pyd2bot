from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredAddedMessage(NetworkMessage):
    ignoreAdded:IgnoredInformations
    session:bool
    
    
