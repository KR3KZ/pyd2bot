from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectMoveKamaMessage(NetworkMessage):
    protocolId = 427
    quantity:float
    
