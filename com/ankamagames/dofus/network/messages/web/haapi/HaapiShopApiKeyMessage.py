from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiShopApiKeyMessage(INetworkMessage):
    protocolId = 6787
    token:str
    
    
