from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseGuildShareRequestMessage(NetworkMessage):
    houseId:int
    instanceId:int
    enable:bool
    rights:int
    
    
