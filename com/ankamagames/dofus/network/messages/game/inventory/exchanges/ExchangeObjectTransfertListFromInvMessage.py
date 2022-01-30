from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectTransfertListFromInvMessage(INetworkMessage):
    protocolId = 3871
    ids:int
    
    
