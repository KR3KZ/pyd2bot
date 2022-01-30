from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiCancelBidRequestMessage(NetworkMessage):
    protocolId = 3479
    id:float
    type:int
    
