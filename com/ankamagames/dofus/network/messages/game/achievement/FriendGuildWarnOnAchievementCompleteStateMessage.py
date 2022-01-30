from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendGuildWarnOnAchievementCompleteStateMessage(INetworkMessage):
    protocolId = 8244
    enable:bool
    
    
