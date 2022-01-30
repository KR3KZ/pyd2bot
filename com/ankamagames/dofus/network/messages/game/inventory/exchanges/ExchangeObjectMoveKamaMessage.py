from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectMoveKamaMessage(INetworkMessage):
    protocolId = 427
    quantity:int
    
    
