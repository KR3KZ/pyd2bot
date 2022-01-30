from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountXpRatioMessage(NetworkMessage):
    protocolId = 1527
    ratio:int
    
    
