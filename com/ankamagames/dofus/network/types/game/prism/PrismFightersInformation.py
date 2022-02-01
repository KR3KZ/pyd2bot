from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightersInformation(INetworkMessage):
    protocolId = 8909
    subAreaId:int
    waitingForHelpInfo:ProtectedEntityWaitingForHelpInfo
    allyCharactersInformations:CharacterMinimalPlusLookInformations
    enemyCharactersInformations:CharacterMinimalPlusLookInformations
    
    
