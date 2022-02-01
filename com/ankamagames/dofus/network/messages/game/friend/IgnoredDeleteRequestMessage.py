from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IgnoredDeleteRequestMessage(NetworkMessage):
    accountId:int
    session:bool
    
    
