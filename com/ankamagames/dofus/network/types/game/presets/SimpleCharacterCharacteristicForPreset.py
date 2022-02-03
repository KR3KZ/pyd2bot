from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SimpleCharacterCharacteristicForPreset(NetworkMessage):
    keyword:str
    base:int
    additionnal:int
    

    def init(self, keyword:str, base:int, additionnal:int):
        self.keyword = keyword
        self.base = base
        self.additionnal = additionnal
        
        super().__init__()
    
    