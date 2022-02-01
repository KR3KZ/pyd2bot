from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonPartyFinderRegisterSuccessMessage(INetworkMessage):
    protocolId = 2385
    dungeonIds:int
    
    
