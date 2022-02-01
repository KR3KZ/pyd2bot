from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendWarnOnLevelGainStateMessage(INetworkMessage):
    protocolId = 7352
    enable:bool
    
    
