from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiValidationMessage(NetworkMessage):
    action:int
    code:int
    

    def init(self, action:int, code:int):
        self.action = action
        self.code = code
        
        super().__init__()
    
    