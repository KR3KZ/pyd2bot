from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeStartOkMulticraftCrafterMessage(INetworkMessage):
    protocolId = 282
    skillId:int
    
    
