from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildMemberWarnOnConnectionStateMessage(INetworkMessage):
    protocolId = 2986
    enable:bool
    
    
