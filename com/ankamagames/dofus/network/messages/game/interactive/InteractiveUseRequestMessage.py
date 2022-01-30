from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InteractiveUseRequestMessage(NetworkMessage):
    protocolId = 9714
    elemId:int
    skillInstanceUid:int
    
