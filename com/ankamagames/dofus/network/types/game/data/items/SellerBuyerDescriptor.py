from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SellerBuyerDescriptor(NetworkMessage):
    protocolId = 5475
    quantities:int
    types:int
    taxPercentage:int
    taxModificationPercentage:int
    maxItemLevel:int
    maxItemPerAccount:int
    npcContextualId:int
    unsoldDelay:int
    
    
