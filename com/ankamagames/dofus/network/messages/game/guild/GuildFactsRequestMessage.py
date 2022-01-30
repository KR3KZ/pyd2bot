from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildFactsRequestMessage(NetworkMessage):
    protocolId = 4628
    guildId:int
    
    
