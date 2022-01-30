from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class IdentificationSuccessMessage(NetworkMessage):
    protocolId = 331
    login:str
    accountTag:AccountTagInformation
    accountId:int
    communityId:int
    secretQuestion:str
    accountCreation:float
    subscriptionElapsedDuration:float
    subscriptionEndDate:float
    havenbagAvailableRoom:int
    
