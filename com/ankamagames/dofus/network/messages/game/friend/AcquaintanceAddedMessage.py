from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation


class AcquaintanceAddedMessage(NetworkMessage):
    protocolId = 6756
    acquaintanceAdded:AcquaintanceInformation
    
    
