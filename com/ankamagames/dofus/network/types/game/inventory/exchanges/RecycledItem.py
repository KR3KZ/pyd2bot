from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class RecycledItem(INetworkMessage):
    protocolId = 161
    id:int
    qty:int
    
    
