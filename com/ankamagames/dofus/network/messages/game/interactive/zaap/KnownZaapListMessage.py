from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class KnownZaapListMessage(NetworkMessage):
    protocolId = 4096
    destinations:list[float]
    
