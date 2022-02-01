from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IdolSelectRequestMessage(INetworkMessage):
    protocolId = 5093
    idolId:int
    activate:bool
    party:bool
    
    
