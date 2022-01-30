from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class FriendJoinRequestMessage(INetworkMessage):
    protocolId = 535
    target:AbstractPlayerSearchInformation
    
    
