from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
    guild:'BasicGuildInformations'
    

    def init(self, guild:'BasicGuildInformations', entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.guild = guild
        
        super().__init__(entityLook, breed, level, name, id)
    
    