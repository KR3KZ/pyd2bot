from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import IdentificationSuccessMessage


class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
    loginToken:str
    
    
