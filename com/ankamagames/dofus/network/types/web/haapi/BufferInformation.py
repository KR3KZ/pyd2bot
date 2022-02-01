from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BufferInformation(INetworkMessage):
    protocolId = 3684
    id:int
    amount:int
    
    
