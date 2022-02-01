from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class AcquaintanceSearchMessage(INetworkMessage):
    protocolId = 9528
    tag:AccountTagInformation
    
    
