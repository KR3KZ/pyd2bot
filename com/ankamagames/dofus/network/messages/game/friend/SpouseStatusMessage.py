from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SpouseStatusMessage(INetworkMessage):
    protocolId = 5406
    hasSpouse:bool
    
    
