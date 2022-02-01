from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class TaxCollectorFightersInformation(NetworkMessage):
    collectorId:int
    allyCharactersInformations:list[CharacterMinimalPlusLookInformations]
    enemyCharactersInformations:list[CharacterMinimalPlusLookInformations]
    
    
