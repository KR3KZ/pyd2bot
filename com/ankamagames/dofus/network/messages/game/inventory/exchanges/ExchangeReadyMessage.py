from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeReadyMessage(NetworkMessage):
    protocolId = 5849
    ready:bool
    step:int
    
