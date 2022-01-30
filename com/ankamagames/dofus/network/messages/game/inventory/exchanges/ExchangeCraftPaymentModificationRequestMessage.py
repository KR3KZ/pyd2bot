from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftPaymentModificationRequestMessage(NetworkMessage):
    protocolId = 5785
    quantity:int
    
    
