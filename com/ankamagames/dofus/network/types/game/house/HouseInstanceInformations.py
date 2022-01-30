from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseInstanceInformations(NetworkMessage):
    protocolId = 3243
    instanceId:int
    ownerTag:AccountTagInformation
    price:float
    
