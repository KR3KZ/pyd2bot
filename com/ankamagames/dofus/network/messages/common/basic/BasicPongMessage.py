from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicPongMessage(INetworkMessage):
    protocolId = 2330
    quiet:bool
    
    
