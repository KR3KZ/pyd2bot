from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendSetWarnOnLevelGainMessage(INetworkMessage):
    protocolId = 4065
    enable:bool
    
    
