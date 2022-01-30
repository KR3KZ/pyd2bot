from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage


class IdentificationFailedBannedMessage(IdentificationFailedMessage):
    protocolId = 4124
    banEndDate:int
    
    
