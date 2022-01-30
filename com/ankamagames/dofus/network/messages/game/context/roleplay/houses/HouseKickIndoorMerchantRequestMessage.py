from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseKickIndoorMerchantRequestMessage(INetworkMessage):
    protocolId = 8862
    cellId:int
    
    
