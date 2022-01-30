from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class FriendDeleteResultMessage(NetworkMessage):
    protocolId = 8619
    success:bool
    tag:AccountTagInformation
    
    
