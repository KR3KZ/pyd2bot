from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IdentificationSuccessMessage(NetworkMessage):
    login:str
    accountTag:'AccountTagInformation'
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
    

    def init(self, login:str, accountTag:'AccountTagInformation', accountId:int, communityId:int, secretQuestion:str, accountCreation:int, subscriptionElapsedDuration:int, subscriptionEndDate:int, havenbagAvailableRoom:int):
        self.login = login
        self.accountTag = accountTag
        self.accountId = accountId
        self.communityId = communityId
        self.secretQuestion = secretQuestion
        self.accountCreation = accountCreation
        self.subscriptionElapsedDuration = subscriptionElapsedDuration
        self.subscriptionEndDate = subscriptionEndDate
        self.havenbagAvailableRoom = havenbagAvailableRoom
        
        super().__init__()
    
    