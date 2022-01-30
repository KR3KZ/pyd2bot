from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BufferInformation(NetworkMessage):
    protocolId = 3684
    id:float
    amount:float
    
