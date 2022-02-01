from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobBookSubscribeRequestMessage(NetworkMessage):
    jobIds:list[int]
    
    
