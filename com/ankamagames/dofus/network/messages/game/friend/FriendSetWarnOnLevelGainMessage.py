from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendSetWarnOnLevelGainMessage(INetworkMessage):
    protocolId = 4065
    enable:bool
    
    
