from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChannelEnablingMessage(NetworkMessage):
    protocolId = 499
    channel:int
    enable:bool
    
    
