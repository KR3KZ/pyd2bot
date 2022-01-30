from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage


class IdentificationAccountForceMessage(IdentificationMessage):
    protocolId = 2449
    forcedAccountLogin:str
    
    
