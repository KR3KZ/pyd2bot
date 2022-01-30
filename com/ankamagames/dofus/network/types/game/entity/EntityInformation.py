from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EntityInformation(NetworkMessage):
    protocolId = 6041
    id:int
    experience:int
    status:bool
    
