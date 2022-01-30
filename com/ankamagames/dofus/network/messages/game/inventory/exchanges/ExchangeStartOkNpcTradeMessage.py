from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeStartOkNpcTradeMessage(INetworkMessage):
    protocolId = 4055
    npcId:int
    
    
