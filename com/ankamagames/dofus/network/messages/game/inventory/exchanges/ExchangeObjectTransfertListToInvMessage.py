from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeObjectTransfertListToInvMessage(INetworkMessage):
    protocolId = 1721
    ids:int
    
    
