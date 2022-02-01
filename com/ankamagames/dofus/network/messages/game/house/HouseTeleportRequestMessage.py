from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseTeleportRequestMessage(NetworkMessage):
    houseId:int
    houseInstanceId:int
    
    
