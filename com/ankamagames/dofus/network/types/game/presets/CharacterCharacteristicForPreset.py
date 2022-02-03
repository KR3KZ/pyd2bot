from com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset


class CharacterCharacteristicForPreset(SimpleCharacterCharacteristicForPreset):
    stuff:int
    

    def init(self, stuff:int, keyword:str, base:int, additionnal:int):
        self.stuff = stuff
        
        super().__init__(keyword, base, additionnal)
    
    