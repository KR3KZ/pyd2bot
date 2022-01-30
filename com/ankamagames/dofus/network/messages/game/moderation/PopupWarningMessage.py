from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PopupWarningMessage(INetworkMessage):
    protocolId = 941
    lockDuration:int
    author:str
    content:str
    
    
