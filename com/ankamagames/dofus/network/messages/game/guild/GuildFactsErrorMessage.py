from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildFactsErrorMessage(INetworkMessage):
    protocolId = 9196
    guildId:int
    
    
