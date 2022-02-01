from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChannelEnablingChangeMessage(NetworkMessage):
    channel:int
    enable:bool
    
    
