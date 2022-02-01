from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeMoneyMovementInformationMessage(INetworkMessage):
    protocolId = 6336
    limit:int
    
    
