from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiSessionMessage(INetworkMessage):
    protocolId = 5486
    key:str
    type:int
    
    
