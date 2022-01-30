from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeOnHumanVendorRequestMessage(INetworkMessage):
    protocolId = 4359
    humanVendorId:int
    humanVendorCell:int
    
    
