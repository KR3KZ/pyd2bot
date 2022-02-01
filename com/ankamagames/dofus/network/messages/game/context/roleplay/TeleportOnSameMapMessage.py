from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportOnSameMapMessage(NetworkMessage):
    targetId:int
    cellId:int
    
    
