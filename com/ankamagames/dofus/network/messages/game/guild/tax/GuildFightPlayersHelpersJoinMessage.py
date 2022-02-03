from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class GuildFightPlayersHelpersJoinMessage(NetworkMessage):
    fightId:int
    playerInfo:'CharacterMinimalPlusLookInformations'
    

    def init(self, fightId:int, playerInfo:'CharacterMinimalPlusLookInformations'):
        self.fightId = fightId
        self.playerInfo = playerInfo
        
        super().__init__()
    
    