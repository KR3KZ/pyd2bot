from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EntityMovementInformations(NetworkMessage):
    protocolId = 7283
    id:int
    steps:list[int]
    
