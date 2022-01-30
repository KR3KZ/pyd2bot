from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildMemberOnlineStatusMessage(NetworkMessage):
    protocolId = 4570
    memberId:float
    online:bool
    
