from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkNpcTradeMessage(NetworkMessage):
    protocolId = 4055
    npcId:float
    
