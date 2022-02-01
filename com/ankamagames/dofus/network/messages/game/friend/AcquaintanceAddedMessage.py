from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation


class AcquaintanceAddedMessage(INetworkMessage):
    protocolId = 6756
    acquaintanceAdded:AcquaintanceInformation
    
    
