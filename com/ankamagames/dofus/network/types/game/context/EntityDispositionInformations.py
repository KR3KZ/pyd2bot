from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EntityDispositionInformations(INetworkMessage):
    protocolId = 7424
    cellId:int
    direction:int
    
    
