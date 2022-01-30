from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildMemberSetWarnOnConnectionMessage(NetworkMessage):
    protocolId = 4147
    enable:bool
    
    
