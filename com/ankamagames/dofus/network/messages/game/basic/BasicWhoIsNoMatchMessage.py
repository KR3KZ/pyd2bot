from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class BasicWhoIsNoMatchMessage(INetworkMessage):
    protocolId = 7631
    target:AbstractPlayerSearchInformation
    
    
