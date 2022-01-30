from com.ankamagames.dofus.network.messages.web.haapi.HaapiValidationMessage import HaapiValidationMessage


class HaapiBuyValidationMessage(HaapiValidationMessage):
    protocolId = 9648
    amount:int
    email:str
    
