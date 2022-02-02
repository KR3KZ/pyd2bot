from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class IdentificationSuccessMessage(NetworkMessage):
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
    
    
    def __post_init__(self):
        super().__init__()
    