from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class CharacterMinimalGuildPublicInformations(CharacterMinimalInformations):
    rank:int
    

    def init(self, rank_:int, level_:int, name_:str, id_:int):
        self.rank = rank_
        
        super().__init__(level_, name_, id_)
    
    