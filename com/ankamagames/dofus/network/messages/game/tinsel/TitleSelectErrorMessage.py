from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TitleSelectErrorMessage(INetworkMessage):
    protocolId = 2014
    reason:int
    
    
