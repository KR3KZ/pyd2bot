from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class FriendDeleteResultMessage(INetworkMessage):
    protocolId = 8619
    success:bool
    tag:AccountTagInformation
    
    
