from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import IdentificationSuccessMessage


class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
    protocolId = 2204
    loginToken:str
    
    
