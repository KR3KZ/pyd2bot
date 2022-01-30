from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildMemberSetWarnOnConnectionMessage(INetworkMessage):
    protocolId = 4147
    enable:bool
    
    
