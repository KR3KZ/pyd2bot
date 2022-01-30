from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildFightLeaveRequestMessage(NetworkMessage):
    protocolId = 5074
    taxCollectorId:float
    characterId:float
    
