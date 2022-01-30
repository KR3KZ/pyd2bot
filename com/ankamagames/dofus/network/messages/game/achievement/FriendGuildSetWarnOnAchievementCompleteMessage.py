from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendGuildSetWarnOnAchievementCompleteMessage(INetworkMessage):
    protocolId = 2644
    enable:bool
    
    
