from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class IgnoredAddRequestMessage(NetworkMessage):
    protocolId = 2801
    target:AbstractPlayerSearchInformation
    session:bool
    
