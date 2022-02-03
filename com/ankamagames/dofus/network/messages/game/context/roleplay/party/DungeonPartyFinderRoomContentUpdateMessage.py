from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
    


class DungeonPartyFinderRoomContentUpdateMessage(NetworkMessage):
    dungeonId:int
    addedPlayers:list['DungeonPartyFinderPlayer']
    removedPlayersIds:list[int]
    

    def init(self, dungeonId:int, addedPlayers:list['DungeonPartyFinderPlayer'], removedPlayersIds:list[int]):
        self.dungeonId = dungeonId
        self.addedPlayers = addedPlayers
        self.removedPlayersIds = removedPlayersIds
        
        super().__init__()
    
    