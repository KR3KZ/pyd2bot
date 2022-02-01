from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CheckIntegrityMessage(INetworkMessage):
    protocolId = 1296
    data:int
    
    
