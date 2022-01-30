from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class RawDataMessage(NetworkMessage):
    protocolId = 6253
    content:bool
    
