from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DocumentReadingBeginMessage(INetworkMessage):
    protocolId = 3768
    documentId:int
    
    
