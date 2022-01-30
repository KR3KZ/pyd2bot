from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CheckFileMessage(NetworkMessage):
    protocolId = 6281
    filenameHash:str
    type:int
    value:str
    
    
