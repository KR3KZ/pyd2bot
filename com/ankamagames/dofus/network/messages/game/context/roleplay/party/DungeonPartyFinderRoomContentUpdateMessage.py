from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer


class DungeonPartyFinderRoomContentUpdateMessage(NetworkMessage):
    protocolId = 6719
    dungeonId:int
    addedPlayers:DungeonPartyFinderPlayer
    removedPlayersIds:int
    
    
