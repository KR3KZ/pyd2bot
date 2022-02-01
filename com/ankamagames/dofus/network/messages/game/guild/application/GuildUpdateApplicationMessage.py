from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildUpdateApplicationMessage(NetworkMessage):
    applyText:str
    guildId:int
    
    
