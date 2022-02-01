from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SellerBuyerDescriptor(NetworkMessage):
    quantities:list[int]
    types:list[int]
    taxPercentage:int
    taxModificationPercentage:int
    maxItemLevel:int
    maxItemPerAccount:int
    npcContextualId:int
    unsoldDelay:int
    
    
