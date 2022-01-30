from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation


class AcquaintancesListMessage(NetworkMessage):
    protocolId = 2842
    acquaintanceList:list[AcquaintanceInformation]
    
