from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer


class DungeonPartyFinderRoomContentUpdateMessage(INetworkMessage):
    protocolId = 6719
    dungeonId:int
    addedPlayers:DungeonPartyFinderPlayer
    removedPlayersIds:int
    
    
