from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class AbstractContactInformations(NetworkMessage):
    protocolId = 6684
    accountId:int
    accountTag:AccountTagInformation
    
    
