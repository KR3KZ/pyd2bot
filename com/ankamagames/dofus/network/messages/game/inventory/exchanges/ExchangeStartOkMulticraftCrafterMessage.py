from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeStartOkMulticraftCrafterMessage(INetworkMessage):
    protocolId = 282
    skillId:int
    
    
