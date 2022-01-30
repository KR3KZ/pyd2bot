from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicPingMessage(NetworkMessage):
    protocolId = 8161
    quiet:bool
    
