from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    livingUID:int
    livingPosition:int
    skinId:int
    
    
