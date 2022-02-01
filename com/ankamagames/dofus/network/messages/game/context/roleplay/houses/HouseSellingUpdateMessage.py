from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseSellingUpdateMessage(NetworkMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    realPrice:int
    buyerTag:AccountTagInformation
    
    
