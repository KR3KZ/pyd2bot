from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectJobAddedMessage(INetworkMessage):
    protocolId = 5325
    jobId:int
    
    
