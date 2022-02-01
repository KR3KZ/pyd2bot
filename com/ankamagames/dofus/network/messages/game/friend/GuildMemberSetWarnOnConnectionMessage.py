from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildMemberSetWarnOnConnectionMessage(INetworkMessage):
    protocolId = 4147
    enable:bool
    
    
