from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation


class AcquaintancesListMessage(NetworkMessage):
    acquaintanceList:list[AcquaintanceInformation]
    
    
