from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CheckFileRequestMessage(INetworkMessage):
    protocolId = 7075
    filename:str
    type:int
    
    
