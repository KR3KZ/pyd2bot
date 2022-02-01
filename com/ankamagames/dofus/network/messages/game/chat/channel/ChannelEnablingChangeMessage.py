from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChannelEnablingChangeMessage(INetworkMessage):
    protocolId = 4041
    channel:int
    enable:bool
    
    
