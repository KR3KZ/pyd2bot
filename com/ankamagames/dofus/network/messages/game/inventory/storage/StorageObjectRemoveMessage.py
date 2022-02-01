from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StorageObjectRemoveMessage(INetworkMessage):
    protocolId = 4970
    objectUID:int
    
    
