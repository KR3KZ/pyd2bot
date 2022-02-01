from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(INetworkMessage):
    protocolId = 5493
    ids:int
    qtys:int
    
    
