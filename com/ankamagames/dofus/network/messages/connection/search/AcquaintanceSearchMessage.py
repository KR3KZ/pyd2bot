from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class AcquaintanceSearchMessage(NetworkMessage):
    protocolId = 9528
    tag:AccountTagInformation
    
    
