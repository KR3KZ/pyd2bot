from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectDeleteMessage(INetworkMessage):
    protocolId = 8147
    objectUID:int
    quantity:int
    
    
