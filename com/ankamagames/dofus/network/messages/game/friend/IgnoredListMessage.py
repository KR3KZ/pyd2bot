from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


class IgnoredListMessage(NetworkMessage):
    ignoredList:list[IgnoredInformations]
    
    
