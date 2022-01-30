from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class WarnOnPermaDeathMessage(INetworkMessage):
    protocolId = 9760
    enable:bool
    
    
