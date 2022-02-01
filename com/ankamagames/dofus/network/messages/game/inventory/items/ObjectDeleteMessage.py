from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectDeleteMessage(NetworkMessage):
    objectUID:int
    quantity:int
    
    
