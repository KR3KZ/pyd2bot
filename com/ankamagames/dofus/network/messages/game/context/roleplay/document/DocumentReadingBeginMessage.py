from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DocumentReadingBeginMessage(INetworkMessage):
    protocolId = 3768
    documentId:int
    
    
