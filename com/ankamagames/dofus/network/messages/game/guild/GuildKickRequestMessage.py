from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildKickRequestMessage(INetworkMessage):
    protocolId = 3965
    kickedId:int
    
    
