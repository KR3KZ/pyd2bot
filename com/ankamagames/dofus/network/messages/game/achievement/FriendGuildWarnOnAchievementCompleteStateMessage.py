from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendGuildWarnOnAchievementCompleteStateMessage(NetworkMessage):
    protocolId = 8244
    enable:bool
    
    
