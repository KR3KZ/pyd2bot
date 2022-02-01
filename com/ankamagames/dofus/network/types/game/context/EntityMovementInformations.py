from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityMovementInformations(NetworkMessage):
    id:int
    steps:list[int]
    
    
