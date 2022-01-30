from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class JobBookSubscription(INetworkMessage):
    protocolId = 6658
    jobId:int
    subscribed:bool
    
    
