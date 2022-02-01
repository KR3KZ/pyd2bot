from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightersInformation(NetworkMessage):
    subAreaId:int
    waitingForHelpInfo:ProtectedEntityWaitingForHelpInfo
    allyCharactersInformations:list[CharacterMinimalPlusLookInformations]
    enemyCharactersInformations:list[CharacterMinimalPlusLookInformations]
    
    
