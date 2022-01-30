from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiValidationRequestMessage(NetworkMessage):
    protocolId = 3931
    transaction:str
    
    
