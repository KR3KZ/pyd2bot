from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameContextRemoveMultipleElementsMessage(INetworkMessage):
    protocolId = 9667
    elementsIds:int
    
    
