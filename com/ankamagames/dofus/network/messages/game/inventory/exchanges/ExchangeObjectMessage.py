from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeObjectMessage(INetworkMessage):
    protocolId = 1966
    remote:bool
    
    
