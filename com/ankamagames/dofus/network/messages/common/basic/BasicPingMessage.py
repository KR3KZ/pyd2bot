from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicPingMessage(INetworkMessage):
    protocolId = 8161
    quiet:bool
    
    
