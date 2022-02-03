from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RemodelingInformation(NetworkMessage):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    

    def init(self, name:str, breed:int, sex:bool, cosmeticId:int, colors:list[int]):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.cosmeticId = cosmeticId
        self.colors = colors
        
        super().__init__()
    
    