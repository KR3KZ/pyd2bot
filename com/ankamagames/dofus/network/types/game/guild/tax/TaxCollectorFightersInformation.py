from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class TaxCollectorFightersInformation(INetworkMessage):
    protocolId = 9650
    collectorId:int
    allyCharactersInformations:CharacterMinimalPlusLookInformations
    enemyCharactersInformations:CharacterMinimalPlusLookInformations
    
    
