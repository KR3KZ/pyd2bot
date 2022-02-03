from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class TaxCollectorFightersInformation(NetworkMessage):
    collectorId:int
    allyCharactersInformations:list['CharacterMinimalPlusLookInformations']
    enemyCharactersInformations:list['CharacterMinimalPlusLookInformations']
    

    def init(self, collectorId:int, allyCharactersInformations:list['CharacterMinimalPlusLookInformations'], enemyCharactersInformations:list['CharacterMinimalPlusLookInformations']):
        self.collectorId = collectorId
        self.allyCharactersInformations = allyCharactersInformations
        self.enemyCharactersInformations = enemyCharactersInformations
        
        super().__init__()
    
    