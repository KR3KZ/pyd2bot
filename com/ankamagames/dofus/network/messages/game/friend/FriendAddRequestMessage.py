from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class FriendAddRequestMessage(INetworkMessage):
    protocolId = 6214
    target:AbstractPlayerSearchInformation
    
    
