from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StatedElement(INetworkMessage):
    protocolId = 7058
    elementId:int
    elementCellId:int
    elementState:int
    onCurrentMap:bool
    
    
