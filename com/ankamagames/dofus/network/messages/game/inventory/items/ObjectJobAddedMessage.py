from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectJobAddedMessage(INetworkMessage):
    protocolId = 5325
    jobId:int
    
    
