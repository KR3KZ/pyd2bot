from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectDropMessage(NetworkMessage):
    objectUID:int
    quantity:int
    
    
