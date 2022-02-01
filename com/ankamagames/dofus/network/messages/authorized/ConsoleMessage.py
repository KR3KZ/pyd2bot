from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ConsoleMessage(INetworkMessage):
    protocolId = 3282
    type:int
    content:str
    
    
