from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TrustCertificate(INetworkMessage):
    protocolId = 8866
    id:int
    hash:str
    
    
