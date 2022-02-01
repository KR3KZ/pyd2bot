from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TitleSelectRequestMessage(INetworkMessage):
    protocolId = 8025
    titleId:int
    
    
