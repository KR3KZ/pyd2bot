from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildFactsRequestMessage(INetworkMessage):
    protocolId = 4628
    guildId:int
    
    
