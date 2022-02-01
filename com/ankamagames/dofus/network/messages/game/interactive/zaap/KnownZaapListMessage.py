from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class KnownZaapListMessage(INetworkMessage):
    protocolId = 4096
    destinations:int
    
    
