from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer


class DungeonPartyFinderRoomContentMessage(INetworkMessage):
    protocolId = 5100
    dungeonId:int
    players:DungeonPartyFinderPlayer
    
    
