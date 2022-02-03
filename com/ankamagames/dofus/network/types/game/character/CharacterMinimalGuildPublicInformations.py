from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class CharacterMinimalGuildPublicInformations(CharacterMinimalInformations):
    rank:int
    

    def init(self, rank:int, level:int, name:str, id:int):
        self.rank = rank
        
        super().__init__(level, name, id)
    
    