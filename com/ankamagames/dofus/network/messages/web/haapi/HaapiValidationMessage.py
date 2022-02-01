from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiValidationMessage(INetworkMessage):
    protocolId = 8710
    action:int
    code:int
    
    
