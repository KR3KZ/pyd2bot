from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PopupWarningMessage(INetworkMessage):
    protocolId = 941
    lockDuration:int
    author:str
    content:str
    
    
