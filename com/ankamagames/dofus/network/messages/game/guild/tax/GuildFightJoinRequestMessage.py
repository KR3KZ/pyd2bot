from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildFightJoinRequestMessage(INetworkMessage):
    protocolId = 9050
    taxCollectorId:int
    
    
