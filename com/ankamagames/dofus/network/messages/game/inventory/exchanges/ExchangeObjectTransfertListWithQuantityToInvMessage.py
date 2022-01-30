from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(NetworkMessage):
    protocolId = 5493
    ids:list[int]
    qtys:list[int]
    
