from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TrustStatusMessage(INetworkMessage):
    protocolId = 8156
    trusted:bool
    certified:bool
    
    
