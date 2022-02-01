from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeStartOkNpcTradeMessage(INetworkMessage):
    protocolId = 4055
    npcId:int
    
    
