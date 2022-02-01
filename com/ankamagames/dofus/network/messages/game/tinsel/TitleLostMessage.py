from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TitleLostMessage(INetworkMessage):
    protocolId = 1427
    titleId:int
    
    
