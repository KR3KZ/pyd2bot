from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CheckFileMessage(INetworkMessage):
    protocolId = 6281
    filenameHash:str
    type:int
    value:str
    
    
