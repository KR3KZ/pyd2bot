from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceChangeGuildRightsMessage(INetworkMessage):
    protocolId = 8453
    guildId:int
    rights:int
    
    
