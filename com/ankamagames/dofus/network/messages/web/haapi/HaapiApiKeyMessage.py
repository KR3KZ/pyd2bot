from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiApiKeyMessage(NetworkMessage):
    protocolId = 9970
    token:str
    
