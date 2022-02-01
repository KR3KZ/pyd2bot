from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class OnConnectionEventMessage(INetworkMessage):
    protocolId = 4485
    eventType:int
    
    
