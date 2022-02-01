from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SequenceNumberMessage(INetworkMessage):
    protocolId = 1059
    number:int
    
    
