from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class RawDataMessage(INetworkMessage):
    protocolId = 6253
    content:bytearray
    
    
