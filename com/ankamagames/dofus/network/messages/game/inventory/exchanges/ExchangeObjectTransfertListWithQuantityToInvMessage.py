from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(INetworkMessage):
    protocolId = 5493
    ids:int
    qtys:int
    
    
