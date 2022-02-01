from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonPartyFinderRegisterRequestMessage(INetworkMessage):
    protocolId = 2723
    dungeonIds:int
    
    
