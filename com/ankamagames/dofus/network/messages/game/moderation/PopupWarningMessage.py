from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PopupWarningMessage(NetworkMessage):
    protocolId = 941
    lockDuration:int
    author:str
    content:str
    
    
