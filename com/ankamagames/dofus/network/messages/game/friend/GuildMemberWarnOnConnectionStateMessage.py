from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildMemberWarnOnConnectionStateMessage(INetworkMessage):
    protocolId = 2986
    enable:bool
    
    
