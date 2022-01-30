from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiValidationRequestMessage(INetworkMessage):
    protocolId = 3931
    transaction:str
    
    
