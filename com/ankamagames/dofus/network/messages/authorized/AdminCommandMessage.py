from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AdminCommandMessage(INetworkMessage):
    protocolId = 4583
    content:str
    
    
