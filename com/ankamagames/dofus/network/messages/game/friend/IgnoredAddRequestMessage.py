from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class IgnoredAddRequestMessage(INetworkMessage):
    protocolId = 2801
    target:AbstractPlayerSearchInformation
    session:bool
    
    
