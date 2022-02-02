from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


@dataclass
class PrismFightersInformation(NetworkMessage):
    subAreaId:int
    waitingForHelpInfo:ProtectedEntityWaitingForHelpInfo
    allyCharactersInformations:list[CharacterMinimalPlusLookInformations]
    enemyCharactersInformations:list[CharacterMinimalPlusLookInformations]
    
    
    def __post_init__(self):
        super().__init__()
    