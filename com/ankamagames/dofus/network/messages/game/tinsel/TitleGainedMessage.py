from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TitleGainedMessage(INetworkMessage):
    protocolId = 3386
    titleId:int
    
    
