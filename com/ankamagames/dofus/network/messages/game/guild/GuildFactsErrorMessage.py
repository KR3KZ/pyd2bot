from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildFactsErrorMessage(INetworkMessage):
    protocolId = 9196
    guildId:int
    
    
