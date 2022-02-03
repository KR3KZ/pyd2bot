from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountCapabilitiesMessage(NetworkMessage):
    accountId:int
    breedsVisible:int
    breedsAvailable:int
    status:int
    tutorialAvailable:bool
    canCreateNewCharacter:bool
    

    def init(self, accountId:int, breedsVisible:int, breedsAvailable:int, status:int):
        self.accountId = accountId
        self.breedsVisible = breedsVisible
        self.breedsAvailable = breedsAvailable
        self.status = status
        
        super().__init__()
    
    