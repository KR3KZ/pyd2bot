from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeStartOkJobIndexMessage(INetworkMessage):
    protocolId = 1146
    jobs:int
    
    
