from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendGuildSetWarnOnAchievementCompleteMessage(NetworkMessage):
    protocolId = 2644
    enable:bool
    
    
