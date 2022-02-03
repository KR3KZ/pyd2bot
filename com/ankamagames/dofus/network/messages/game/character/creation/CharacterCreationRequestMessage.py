from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCreationRequestMessage(NetworkMessage):
    name:str
    breed:int
    sex:bool
    colors:list[int]
    cosmeticId:int
    

    def init(self, name:str, breed:int, sex:bool, colors:list[int], cosmeticId:int):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.colors = colors
        self.cosmeticId = cosmeticId
        
        super().__init__()
    
    