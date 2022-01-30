from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ConsoleMessage(INetworkMessage):
    protocolId = 3282
    type:int
    content:str
    
    
