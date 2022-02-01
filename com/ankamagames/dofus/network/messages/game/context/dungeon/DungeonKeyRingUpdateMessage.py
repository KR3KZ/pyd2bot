from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonKeyRingUpdateMessage(NetworkMessage):
    dungeonId:int
    available:bool
    
    
