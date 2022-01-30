from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class AbstractContactInformations(INetworkMessage):
    protocolId = 6684
    accountId:int
    accountTag:AccountTagInformation
    
    
