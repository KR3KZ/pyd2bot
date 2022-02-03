from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage


class IdentificationFailedBannedMessage(IdentificationFailedMessage):
    banEndDate:int
    

    def init(self, banEndDate:int, reason:int):
        self.banEndDate = banEndDate
        
        super().__init__(reason)
    
    