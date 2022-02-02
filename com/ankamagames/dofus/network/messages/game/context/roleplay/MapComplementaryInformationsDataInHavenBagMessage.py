from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


@dataclass
class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
    ownerInformations:CharacterMinimalInformations
    theme:int
    roomId:int
    maxRoomId:int
    
    
    def __post_init__(self):
        super().__init__()
    