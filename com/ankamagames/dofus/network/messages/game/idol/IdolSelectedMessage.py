from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IdolSelectedMessage(INetworkMessage):
    protocolId = 7348
    idolId:int
    activate:bool
    party:bool
    
    
