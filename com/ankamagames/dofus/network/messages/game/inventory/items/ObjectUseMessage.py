from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectUseMessage(INetworkMessage):
    protocolId = 3065
    objectUID:int
    
    
