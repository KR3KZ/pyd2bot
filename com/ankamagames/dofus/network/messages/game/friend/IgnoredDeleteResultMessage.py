from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class IgnoredDeleteResultMessage(NetworkMessage):
    protocolId = 9652
    tag:AccountTagInformation
    success:bool
    session:bool
    
    
