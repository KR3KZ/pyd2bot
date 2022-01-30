from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChannelEnablingChangeMessage(INetworkMessage):
    protocolId = 4041
    channel:int
    enable:bool
    
    
