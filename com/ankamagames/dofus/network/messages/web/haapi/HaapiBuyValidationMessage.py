from com.ankamagames.dofus.network.messages.web.haapi.HaapiValidationMessage import HaapiValidationMessage


class HaapiBuyValidationMessage(HaapiValidationMessage):
    amount:int
    email:str
    

    def init(self, amount:int, email:str, action:int, code:int):
        self.amount = amount
        self.email = email
        
        super().__init__(action, code)
    
    