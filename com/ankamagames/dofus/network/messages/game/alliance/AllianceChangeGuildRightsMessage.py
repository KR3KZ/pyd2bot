from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceChangeGuildRightsMessage(INetworkMessage):
    protocolId = 8453
    guildId:int
    rights:int
    
    
