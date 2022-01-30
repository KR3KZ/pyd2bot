from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildMemberWarnOnConnectionStateMessage(NetworkMessage):
    protocolId = 2986
    enable:bool
    
    
