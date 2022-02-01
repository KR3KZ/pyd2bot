from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeMapMessage(NetworkMessage):
    mapId:int
    autopilot:bool
    
    
