from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountSetXpRatioRequestMessage(NetworkMessage):
    protocolId = 9275
    xpRatio:int
    
