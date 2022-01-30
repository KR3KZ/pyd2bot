from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class WarnOnPermaDeathStateMessage(INetworkMessage):
    protocolId = 8629
    enable:bool
    
    
