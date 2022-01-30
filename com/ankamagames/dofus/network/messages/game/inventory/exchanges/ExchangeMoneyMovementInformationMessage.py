from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMoneyMovementInformationMessage(NetworkMessage):
    protocolId = 6336
    limit:int
    
