from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HelloConnectMessage(INetworkMessage):
    protocolId = 6739
    salt:str
    key:int
    
    
