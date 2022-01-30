from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiCancelBidRequestMessage(INetworkMessage):
    protocolId = 3479
    id:int
    type:int
    
    
