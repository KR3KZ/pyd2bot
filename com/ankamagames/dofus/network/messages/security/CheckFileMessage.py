from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckFileMessage(NetworkMessage):
    filenameHash:str
    type:int
    value:str
    
    
