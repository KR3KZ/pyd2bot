from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation


class AcquaintanceAddedMessage(NetworkMessage):
    acquaintanceAdded:AcquaintanceInformation
    
    
