from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class BasicWhoIsRequestMessage(NetworkMessage):
    protocolId = 1784
    verbose:bool
    target:AbstractPlayerSearchInformation
    
