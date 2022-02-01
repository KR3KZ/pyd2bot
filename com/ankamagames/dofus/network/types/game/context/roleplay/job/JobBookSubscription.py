from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class JobBookSubscription(INetworkMessage):
    protocolId = 6658
    jobId:int
    subscribed:bool
    
    
