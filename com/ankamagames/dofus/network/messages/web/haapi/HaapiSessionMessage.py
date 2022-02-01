from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiSessionMessage(INetworkMessage):
    protocolId = 5486
    key:str
    type:int
    
    
