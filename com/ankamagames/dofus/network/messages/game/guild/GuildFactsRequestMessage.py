from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildFactsRequestMessage(INetworkMessage):
    protocolId = 4628
    guildId:int
    
    
