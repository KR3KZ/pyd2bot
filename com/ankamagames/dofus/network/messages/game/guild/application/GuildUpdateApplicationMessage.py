from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildUpdateApplicationMessage(NetworkMessage):
    protocolId = 6940
    applyText:str
    guildId:int
    
    
