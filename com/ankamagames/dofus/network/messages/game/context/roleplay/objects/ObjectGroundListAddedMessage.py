from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectGroundListAddedMessage(INetworkMessage):
    protocolId = 6617
    cells:int
    referenceIds:int
    
    
