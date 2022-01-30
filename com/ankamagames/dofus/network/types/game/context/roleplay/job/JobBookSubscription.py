from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class JobBookSubscription(NetworkMessage):
    protocolId = 6658
    jobId:int
    subscribed:bool
    
    
