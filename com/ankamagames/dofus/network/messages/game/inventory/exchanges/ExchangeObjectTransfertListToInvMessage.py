from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListToInvMessage(NetworkMessage):
    protocolId = 1721
    ids:list[int]
    
