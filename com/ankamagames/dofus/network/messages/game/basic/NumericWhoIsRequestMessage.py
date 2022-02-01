from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NumericWhoIsRequestMessage(INetworkMessage):
    protocolId = 4159
    playerId:int
    
    
