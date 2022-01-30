from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer


class DungeonPartyFinderRoomContentMessage(NetworkMessage):
    protocolId = 5100
    dungeonId:int
    players:DungeonPartyFinderPlayer
    
    
