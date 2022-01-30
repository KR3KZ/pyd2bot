from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DocumentReadingBeginMessage(NetworkMessage):
    protocolId = 3768
    documentId:int
    
    
