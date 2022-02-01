from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SellerBuyerDescriptor(INetworkMessage):
    protocolId = 5475
    quantities:int
    types:int
    taxPercentage:int
    taxModificationPercentage:int
    maxItemLevel:int
    maxItemPerAccount:int
    npcContextualId:int
    unsoldDelay:int
    
    
