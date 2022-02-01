from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameContextRemoveMultipleElementsMessage(INetworkMessage):
    protocolId = 9667
    elementsIds:int
    
    
