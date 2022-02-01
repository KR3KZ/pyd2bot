from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class AbstractContactInformations(NetworkMessage):
    accountId:int
    accountTag:AccountTagInformation
    
    
