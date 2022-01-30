from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class IdentificationSuccessMessage(INetworkMessage):
    protocolId = 331
    login:str
    accountTag:AccountTagInformation
    accountId:int
    communityId:int
    secretQuestion:str
    accountCreation:int
    subscriptionElapsedDuration:int
    subscriptionEndDate:int
    havenbagAvailableRoom:int
    hasRights:bool
    hasConsoleRight:bool
    wasAlreadyConnected:bool
    
    
