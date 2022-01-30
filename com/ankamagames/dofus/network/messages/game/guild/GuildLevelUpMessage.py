from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildLevelUpMessage(INetworkMessage):
    protocolId = 7669
    newLevel:int
    
    
