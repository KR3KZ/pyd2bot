from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ClientKeyMessage(INetworkMessage):
    protocolId = 7137
    key:str
    
    
