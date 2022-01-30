from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TrustStatusMessage(NetworkMessage):
    protocolId = 8156
    trusted:bool
    certified:bool
    
    
