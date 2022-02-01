from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildJoinAutomaticallyRequestMessage(INetworkMessage):
    protocolId = 6478
    guildId:int
    
    
