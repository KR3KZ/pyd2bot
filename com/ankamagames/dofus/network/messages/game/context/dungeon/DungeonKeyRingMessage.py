from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DungeonKeyRingMessage(INetworkMessage):
    protocolId = 6497
    availables:int
    unavailables:int
    
    
