from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachEnterMessage(INetworkMessage):
    protocolId = 6485
    owner:int
    
    
