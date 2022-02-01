from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildMemberLeavingMessage(INetworkMessage):
    protocolId = 419
    kicked:bool
    memberId:int
    
    
