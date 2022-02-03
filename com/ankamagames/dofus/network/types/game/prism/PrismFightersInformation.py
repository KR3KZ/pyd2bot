from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class PrismFightersInformation(NetworkMessage):
    subAreaId:int
    waitingForHelpInfo:'ProtectedEntityWaitingForHelpInfo'
    allyCharactersInformations:list['CharacterMinimalPlusLookInformations']
    enemyCharactersInformations:list['CharacterMinimalPlusLookInformations']
    

    def init(self, subAreaId:int, waitingForHelpInfo:'ProtectedEntityWaitingForHelpInfo', allyCharactersInformations:list['CharacterMinimalPlusLookInformations'], enemyCharactersInformations:list['CharacterMinimalPlusLookInformations']):
        self.subAreaId = subAreaId
        self.waitingForHelpInfo = waitingForHelpInfo
        self.allyCharactersInformations = allyCharactersInformations
        self.enemyCharactersInformations = enemyCharactersInformations
        
        super().__init__()
    
    