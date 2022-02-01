from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonKeyRingUpdateMessage(INetworkMessage):
    protocolId = 2874
    dungeonId:int
    available:bool
    
    
