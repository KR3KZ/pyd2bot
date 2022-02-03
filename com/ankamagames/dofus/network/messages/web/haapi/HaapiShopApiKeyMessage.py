from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiShopApiKeyMessage(NetworkMessage):
    token:str
    

    def init(self, token:str):
        self.token = token
        
        super().__init__()
    
    