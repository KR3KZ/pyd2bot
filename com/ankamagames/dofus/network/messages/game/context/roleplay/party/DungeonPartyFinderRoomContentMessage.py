from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer


class DungeonPartyFinderRoomContentMessage(NetworkMessage):
    dungeonId:int
    players:list[DungeonPartyFinderPlayer]
    
    
