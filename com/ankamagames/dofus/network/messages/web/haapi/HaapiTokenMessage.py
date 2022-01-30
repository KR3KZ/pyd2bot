from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HaapiTokenMessage(INetworkMessage):
    protocolId = 8938
    token:str
    
    
