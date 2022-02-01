from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PopupWarningMessage(NetworkMessage):
    lockDuration:int
    author:str
    content:str
    
    
