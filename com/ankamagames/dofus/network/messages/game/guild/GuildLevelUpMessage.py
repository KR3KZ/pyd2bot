from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildLevelUpMessage(NetworkMessage):
    protocolId = 7669
    newLevel:int
    
    
