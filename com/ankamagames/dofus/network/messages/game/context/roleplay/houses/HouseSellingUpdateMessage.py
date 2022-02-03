from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseSellingUpdateMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    realPrice:int
    buyerTag:'AccountTagInformation'
    

    def init(self, houseId:int, instanceId:int, secondHand:bool, realPrice:int, buyerTag:'AccountTagInformation'):
        self.houseId = houseId
        self.instanceId = instanceId
        self.secondHand = secondHand
        self.realPrice = realPrice
        self.buyerTag = buyerTag
        
        super().__init__()
    
    