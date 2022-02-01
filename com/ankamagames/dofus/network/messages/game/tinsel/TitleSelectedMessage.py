from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TitleSelectedMessage(INetworkMessage):
    protocolId = 8922
    titleId:int
    
    
