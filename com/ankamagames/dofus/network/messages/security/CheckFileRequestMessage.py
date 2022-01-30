from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CheckFileRequestMessage(NetworkMessage):
    protocolId = 7075
    filename:str
    type:int
    
    
