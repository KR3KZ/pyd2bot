from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ActorOrientation(INetworkMessage):
    protocolId = 6459
    id:int
    direction:int
    
    
