from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkJobIndexMessage(NetworkMessage):
    protocolId = 1146
    jobs:list[int]
    
