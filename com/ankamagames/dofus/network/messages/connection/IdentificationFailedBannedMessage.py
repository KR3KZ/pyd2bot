from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage


class IdentificationFailedBannedMessage(IdentificationFailedMessage):
    banEndDate:int
    
    
