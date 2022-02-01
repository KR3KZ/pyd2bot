from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
    ownerInformations:CharacterMinimalInformations
    theme:int
    roomId:int
    maxRoomId:int
    
    
