from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InteractiveUseEndedMessage(NetworkMessage):
    protocolId = 4234
    elemId:int
    skillId:int
    
    
