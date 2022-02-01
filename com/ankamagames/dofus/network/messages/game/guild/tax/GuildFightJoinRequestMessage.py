from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildFightJoinRequestMessage(INetworkMessage):
    protocolId = 9050
    taxCollectorId:int
    
    
