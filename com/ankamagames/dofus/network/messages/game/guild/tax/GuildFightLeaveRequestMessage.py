from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildFightLeaveRequestMessage(INetworkMessage):
    protocolId = 5074
    taxCollectorId:int
    characterId:int
    
    
