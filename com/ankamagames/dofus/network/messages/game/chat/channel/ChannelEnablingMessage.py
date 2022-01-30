from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChannelEnablingMessage(INetworkMessage):
    protocolId = 499
    channel:int
    enable:bool
    
    
