from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalAllianceInformations(CharacterMinimalGuildInformations):
    alliance:'BasicAllianceInformations'
    

    def init(self, alliance:'BasicAllianceInformations', guild:'BasicGuildInformations', entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.alliance = alliance
        
        super().__init__(guild, entityLook, breed, level, name, id)
    
    