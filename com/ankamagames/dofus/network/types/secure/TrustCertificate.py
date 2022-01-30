from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TrustCertificate(INetworkMessage):
    protocolId = 8866
    id:int
    hash:str
    
    
