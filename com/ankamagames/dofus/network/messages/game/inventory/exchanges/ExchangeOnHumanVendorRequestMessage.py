from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeOnHumanVendorRequestMessage(INetworkMessage):
    protocolId = 4359
    humanVendorId:int
    humanVendorCell:int
    
    
