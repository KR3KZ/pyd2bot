from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HelloConnectMessage(NetworkMessage):
    salt:str
    key:list[int]
    
    
