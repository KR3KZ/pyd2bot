from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameContextRemoveMultipleElementsMessage(NetworkMessage):
    protocolId = 9667
    elementsIds:int
    
    
