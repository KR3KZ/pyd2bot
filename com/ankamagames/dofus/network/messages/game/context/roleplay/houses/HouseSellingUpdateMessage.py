from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseSellingUpdateMessage(NetworkMessage):
    protocolId = 3951
    houseId:int
    instanceId:int
    secondHand:bool
    realPrice:float
    buyerTag:AccountTagInformation
    
