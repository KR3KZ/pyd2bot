from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChannelEnablingMessage(INetworkMessage):
    protocolId = 499
    channel:int
    enable:bool
    
    
