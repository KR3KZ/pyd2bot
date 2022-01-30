from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountRidingMessage(INetworkMessage):
    protocolId = 6231
    isRiding:bool
    isAutopilot:bool
    
    
