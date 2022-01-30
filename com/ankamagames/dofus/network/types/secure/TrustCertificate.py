from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TrustCertificate(NetworkMessage):
    protocolId = 8866
    id:int
    hash:str
    
    
