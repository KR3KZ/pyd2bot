from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HelloConnectMessage(INetworkMessage):
    protocolId = 6739
    salt:str
    key:int
    
    
