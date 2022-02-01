from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StorageObjectsRemoveMessage(INetworkMessage):
    protocolId = 7044
    objectUIDList:int
    
    
