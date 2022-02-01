from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChatAbstractClientMessage(INetworkMessage):
    protocolId = 1037
    content:str
    
    
