from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildModificationNameValidMessage(NetworkMessage):
    protocolId = 5982
    guildName:str
    
    
