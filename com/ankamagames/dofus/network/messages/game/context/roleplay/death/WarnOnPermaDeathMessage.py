from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class WarnOnPermaDeathMessage(NetworkMessage):
    protocolId = 9760
    enable:bool
    
