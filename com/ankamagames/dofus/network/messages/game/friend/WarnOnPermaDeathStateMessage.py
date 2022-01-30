from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class WarnOnPermaDeathStateMessage(NetworkMessage):
    protocolId = 8629
    enable:bool
    
