from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicPongMessage(NetworkMessage):
    protocolId = 2330
    quiet:bool
    
