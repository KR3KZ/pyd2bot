from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendGuildSetWarnOnAchievementCompleteMessage(INetworkMessage):
    protocolId = 2644
    enable:bool
    
    
