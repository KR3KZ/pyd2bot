from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import IdentificationSuccessMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
    loginToken:str
    

    def init(self, loginToken:str, login:str, accountTag:'AccountTagInformation', accountId:int, communityId:int, secretQuestion:str, accountCreation:int, subscriptionElapsedDuration:int, subscriptionEndDate:int, havenbagAvailableRoom:int):
        self.loginToken = loginToken
        
        super().__init__(login, accountTag, accountId, communityId, secretQuestion, accountCreation, subscriptionElapsedDuration, subscriptionEndDate, havenbagAvailableRoom)
    
    