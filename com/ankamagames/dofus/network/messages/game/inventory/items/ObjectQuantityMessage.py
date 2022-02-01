from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectQuantityMessage(NetworkMessage):
    objectUID:int
    quantity:int
    origin:int
    
    
