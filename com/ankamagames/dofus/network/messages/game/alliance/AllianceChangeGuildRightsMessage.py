from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceChangeGuildRightsMessage(NetworkMessage):
    protocolId = 8453
    guildId:int
    rights:int
    
