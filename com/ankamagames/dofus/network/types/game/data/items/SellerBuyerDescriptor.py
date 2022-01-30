from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SellerBuyerDescriptor(NetworkMessage):
    protocolId = 5475
    quantities:list[int]
    types:list[int]
    taxPercentage:float
    taxModificationPercentage:float
    maxItemLevel:int
    maxItemPerAccount:int
    npcContextualId:int
    unsoldDelay:int
    
