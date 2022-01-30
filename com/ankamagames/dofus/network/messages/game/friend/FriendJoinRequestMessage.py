from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class FriendJoinRequestMessage(NetworkMessage):
    protocolId = 535
    target:AbstractPlayerSearchInformation
    
    
