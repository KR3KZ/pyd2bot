from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class TaxCollectorFightersInformation(NetworkMessage):
    protocolId = 9650
    collectorId:int
    allyCharactersInformations:CharacterMinimalPlusLookInformations
    enemyCharactersInformations:CharacterMinimalPlusLookInformations
    
    
