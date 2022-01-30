from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountRidingMessage(NetworkMessage):
    protocolId = 6231
    isRiding:bool
    isAutopilot:bool
    
    
