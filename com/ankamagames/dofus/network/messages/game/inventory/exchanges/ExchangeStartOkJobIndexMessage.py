from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeStartOkJobIndexMessage(INetworkMessage):
    protocolId = 1146
    jobs:int
    
    
