from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectsDeletedMessage(INetworkMessage):
    protocolId = 9871
    objectUID:int
    
    
