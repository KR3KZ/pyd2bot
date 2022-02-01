from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachKickRequestMessage(INetworkMessage):
    protocolId = 2909
    target:int
    
    
