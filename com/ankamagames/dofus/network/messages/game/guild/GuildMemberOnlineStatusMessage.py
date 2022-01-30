from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildMemberOnlineStatusMessage(INetworkMessage):
    protocolId = 4570
    memberId:int
    online:bool
    
    
