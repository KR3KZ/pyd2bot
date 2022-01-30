from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCrafterMessage(NetworkMessage):
    protocolId = 282
    skillId:int
    
    
