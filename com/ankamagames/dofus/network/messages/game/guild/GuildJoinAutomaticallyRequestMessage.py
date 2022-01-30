from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildJoinAutomaticallyRequestMessage(INetworkMessage):
    protocolId = 6478
    guildId:int
    
    
