from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiCancelBidRequestMessage(INetworkMessage):
    protocolId = 3479
    id:int
    type:int
    
    
