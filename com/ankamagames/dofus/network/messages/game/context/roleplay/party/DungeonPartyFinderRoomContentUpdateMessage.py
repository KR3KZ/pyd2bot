from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer


class DungeonPartyFinderRoomContentUpdateMessage(NetworkMessage):
    dungeonId:int
    addedPlayers:list[DungeonPartyFinderPlayer]
    removedPlayersIds:list[int]
    
    
