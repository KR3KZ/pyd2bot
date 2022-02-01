from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IdentificationFailedMessage(INetworkMessage):
    protocolId = 7135
    reason:int
    
    
