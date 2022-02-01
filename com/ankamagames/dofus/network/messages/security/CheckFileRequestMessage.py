from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CheckFileRequestMessage(INetworkMessage):
    protocolId = 7075
    filename:str
    type:int
    
    
