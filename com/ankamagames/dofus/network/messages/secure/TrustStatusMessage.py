from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TrustStatusMessage(INetworkMessage):
    protocolId = 8156
    trusted:bool
    certified:bool
    
    
