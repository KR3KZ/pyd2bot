from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class FriendAddRequestMessage(NetworkMessage):
    protocolId = 6214
    target:AbstractPlayerSearchInformation
    
    
