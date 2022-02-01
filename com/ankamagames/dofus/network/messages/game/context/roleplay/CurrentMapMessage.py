from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CurrentMapMessage(INetworkMessage):
    protocolId = 9325
    mapId:int
    mapKey:str
    
    
