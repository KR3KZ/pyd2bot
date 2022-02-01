from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HaapiConfirmationRequestMessage(INetworkMessage):
    protocolId = 5599
    kamas:int
    ogrines:int
    rate:int
    action:int
    
    
