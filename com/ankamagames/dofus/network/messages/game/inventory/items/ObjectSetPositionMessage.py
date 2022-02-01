from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectSetPositionMessage(NetworkMessage):
    objectUID:int
    position:int
    quantity:int
    
    
