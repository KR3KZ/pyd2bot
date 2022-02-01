from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiValidationRequestMessage(INetworkMessage):
    protocolId = 3931
    transaction:str
    
    
