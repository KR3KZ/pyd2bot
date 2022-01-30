from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeOnHumanVendorRequestMessage(NetworkMessage):
    protocolId = 4359
    humanVendorId:int
    humanVendorCell:int
    
    
