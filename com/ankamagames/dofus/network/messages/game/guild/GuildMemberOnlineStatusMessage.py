from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildMemberOnlineStatusMessage(INetworkMessage):
    protocolId = 4570
    memberId:int
    online:bool
    
    
