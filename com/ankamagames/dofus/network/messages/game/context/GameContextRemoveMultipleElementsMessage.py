from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextRemoveMultipleElementsMessage(NetworkMessage):
    elementsIds:list[int]
    
    
