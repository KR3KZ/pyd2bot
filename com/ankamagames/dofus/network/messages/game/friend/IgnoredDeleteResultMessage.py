from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class IgnoredDeleteResultMessage(NetworkMessage):
    tag:AccountTagInformation
    success:bool
    session:bool
    
    
