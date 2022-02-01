from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseSellingUpdateMessage(INetworkMessage):
    protocolId = 3951
    houseId:int
    instanceId:int
    secondHand:bool
    realPrice:int
    buyerTag:AccountTagInformation
    
    
