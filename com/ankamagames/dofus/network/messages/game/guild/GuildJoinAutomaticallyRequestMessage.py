from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildJoinAutomaticallyRequestMessage(NetworkMessage):
    protocolId = 6478
    guildId:int
    
