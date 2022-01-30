from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HaapiShopApiKeyMessage(NetworkMessage):
    protocolId = 6787
    token:str
    
    
