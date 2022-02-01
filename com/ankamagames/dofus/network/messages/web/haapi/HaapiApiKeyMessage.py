from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiApiKeyMessage(INetworkMessage):
    protocolId = 9970
    token:str
    
    
