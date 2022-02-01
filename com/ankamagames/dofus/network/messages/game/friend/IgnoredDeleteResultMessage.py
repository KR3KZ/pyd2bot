from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class IgnoredDeleteResultMessage(INetworkMessage):
    protocolId = 9652
    tag:AccountTagInformation
    success:bool
    session:bool
    
    
