from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountSetXpRatioRequestMessage(INetworkMessage):
    protocolId = 9275
    xpRatio:int
    
    
