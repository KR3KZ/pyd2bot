from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(NetworkMessage):
    ids:list[int]
    qtys:list[int]
    
    
