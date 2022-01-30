from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectMessage(NetworkMessage):
    protocolId = 1966
    remote:bool
    
