from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountEquipedErrorMessage(NetworkMessage):
    protocolId = 1774
    errorType:int
    
    
