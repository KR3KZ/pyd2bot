from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class PlayerSearchCharacterNameInformation(AbstractPlayerSearchInformation):
    name:str
    

    def init(self, name:str):
        self.name = name
        
        super().__init__()
    
    