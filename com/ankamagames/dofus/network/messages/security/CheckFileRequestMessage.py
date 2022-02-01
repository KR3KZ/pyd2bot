from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckFileRequestMessage(NetworkMessage):
    filename:str
    type:int
    
    
