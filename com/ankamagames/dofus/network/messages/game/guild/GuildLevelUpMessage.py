from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildLevelUpMessage(INetworkMessage):
    protocolId = 7669
    newLevel:int
    
    
