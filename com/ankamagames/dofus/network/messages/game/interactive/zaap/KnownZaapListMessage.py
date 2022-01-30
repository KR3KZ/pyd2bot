from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class KnownZaapListMessage(INetworkMessage):
    protocolId = 4096
    destinations:int
    
    
