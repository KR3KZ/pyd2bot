from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class BasicWhoIsRequestMessage(INetworkMessage):
    protocolId = 1784
    verbose:bool
    target:AbstractPlayerSearchInformation
    
    
