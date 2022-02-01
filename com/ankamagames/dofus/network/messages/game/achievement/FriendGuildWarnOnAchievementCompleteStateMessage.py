from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendGuildWarnOnAchievementCompleteStateMessage(INetworkMessage):
    protocolId = 8244
    enable:bool
    
    
