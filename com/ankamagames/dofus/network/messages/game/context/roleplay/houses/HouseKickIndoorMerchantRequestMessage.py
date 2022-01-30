from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseKickIndoorMerchantRequestMessage(NetworkMessage):
    protocolId = 8862
    cellId:int
    
