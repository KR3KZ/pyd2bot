from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectItemInRolePlay(NetworkMessage):
    protocolId = 4848
    cellId:int
    objectGID:int
    
    
