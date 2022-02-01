from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachExitResponseMessage(INetworkMessage):
    protocolId = 7143
    exited:bool
    
    
