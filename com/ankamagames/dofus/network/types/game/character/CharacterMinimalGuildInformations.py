from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
    protocolId = 4548
    guild:BasicGuildInformations
    
    
