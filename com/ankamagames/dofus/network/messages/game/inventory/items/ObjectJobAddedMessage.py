from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectJobAddedMessage(NetworkMessage):
    protocolId = 5325
    jobId:int
    
