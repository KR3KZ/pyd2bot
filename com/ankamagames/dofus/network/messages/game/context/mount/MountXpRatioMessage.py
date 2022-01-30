from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountXpRatioMessage(INetworkMessage):
    protocolId = 1527
    ratio:int
    
    
