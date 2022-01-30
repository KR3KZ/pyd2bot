from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListFromInvMessage(NetworkMessage):
    protocolId = 3871
    ids:list[int]
    
