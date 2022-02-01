from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectsDeletedMessage(NetworkMessage):
    objectUID:list[int]
    
    
