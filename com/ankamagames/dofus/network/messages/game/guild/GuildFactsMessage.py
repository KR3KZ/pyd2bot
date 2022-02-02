from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations


@dataclass
class GuildFactsMessage(NetworkMessage):
    infos:GuildFactSheetInformations
    creationDate:int
    nbTaxCollectors:int
    members:list[CharacterMinimalGuildPublicInformations]
    
    
    def __post_init__(self):
        super().__init__()
    