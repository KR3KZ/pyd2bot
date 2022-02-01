from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundListAddedMessage(NetworkMessage):
    cells:list[int]
    referenceIds:list[int]
    
    
