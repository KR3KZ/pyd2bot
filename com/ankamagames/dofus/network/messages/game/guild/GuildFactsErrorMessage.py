from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildFactsErrorMessage(NetworkMessage):
    protocolId = 9196
    guildId:int
    
