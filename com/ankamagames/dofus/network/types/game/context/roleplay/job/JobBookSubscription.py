from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobBookSubscription(NetworkMessage):
    jobId:int
    subscribed:bool
    
    
