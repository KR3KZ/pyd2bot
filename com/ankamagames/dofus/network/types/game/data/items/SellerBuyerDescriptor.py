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
    

    def init(self, quantities:list[int], types:list[int], taxPercentage:int, taxModificationPercentage:int, maxItemLevel:int, maxItemPerAccount:int, npcContextualId:int, unsoldDelay:int):
        self.quantities = quantities
        self.types = types
        self.taxPercentage = taxPercentage
        self.taxModificationPercentage = taxModificationPercentage
        self.maxItemLevel = maxItemLevel
        self.maxItemPerAccount = maxItemPerAccount
        self.npcContextualId = npcContextualId
        self.unsoldDelay = unsoldDelay
        
        super().__init__()
    
    