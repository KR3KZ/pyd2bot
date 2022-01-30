from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChannelEnablingChangeMessage(NetworkMessage):
    protocolId = 4041
    channel:int
    enable:bool
    
    
