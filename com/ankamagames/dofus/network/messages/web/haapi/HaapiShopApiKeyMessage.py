from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiShopApiKeyMessage(INetworkMessage):
    protocolId = 6787
    token:str
    
    
