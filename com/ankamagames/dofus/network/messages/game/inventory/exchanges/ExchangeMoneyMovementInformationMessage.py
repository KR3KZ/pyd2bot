from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMoneyMovementInformationMessage(INetworkMessage):
    protocolId = 6336
    limit:int
    
    
