from com.ankamagames.dofus.network.messages.web.haapi.HaapiValidationMessage import HaapiValidationMessage


class HaapiBuyValidationMessage(HaapiValidationMessage):
    amount:int
    email:str
    
    
