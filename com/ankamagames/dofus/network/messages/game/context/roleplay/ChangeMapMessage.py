from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChangeMapMessage(INetworkMessage):
    protocolId = 3431
    mapId:int
    autopilot:bool
    
    
