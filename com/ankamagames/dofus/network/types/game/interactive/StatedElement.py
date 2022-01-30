from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StatedElement(NetworkMessage):
    protocolId = 7058
    elementId:int
    elementCellId:int
    elementState:int
    onCurrentMap:bool
    
