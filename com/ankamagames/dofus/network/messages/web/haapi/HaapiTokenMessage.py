from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiTokenMessage(INetworkMessage):
    protocolId = 8938
    token:str
    
    
