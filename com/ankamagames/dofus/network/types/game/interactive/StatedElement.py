from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatedElement(NetworkMessage):
    elementId:int
    elementCellId:int
    elementState:int
    onCurrentMap:bool
    
    
