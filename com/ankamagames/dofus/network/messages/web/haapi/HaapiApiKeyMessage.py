from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiApiKeyMessage(INetworkMessage):
    protocolId = 9970
    token:str
    
    
