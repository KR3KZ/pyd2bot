from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
    entityLook:EntityLook
    breed:int
    
    
