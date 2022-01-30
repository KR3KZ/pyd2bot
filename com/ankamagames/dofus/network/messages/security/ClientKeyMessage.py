from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ClientKeyMessage(INetworkMessage):
    protocolId = 7137
    key:str
    
    
