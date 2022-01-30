from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildFightJoinRequestMessage(NetworkMessage):
    protocolId = 9050
    taxCollectorId:int
    
    
