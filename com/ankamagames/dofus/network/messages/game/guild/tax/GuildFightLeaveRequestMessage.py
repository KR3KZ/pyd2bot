from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildFightLeaveRequestMessage(INetworkMessage):
    protocolId = 5074
    taxCollectorId:int
    characterId:int
    
    
