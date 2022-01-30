from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InteractiveUseErrorMessage(NetworkMessage):
    protocolId = 778
    elemId:int
    skillInstanceUid:int
    
