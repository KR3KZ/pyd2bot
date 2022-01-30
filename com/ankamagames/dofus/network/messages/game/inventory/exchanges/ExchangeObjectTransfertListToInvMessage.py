from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectTransfertListToInvMessage(INetworkMessage):
    protocolId = 1721
    ids:int
    
    
