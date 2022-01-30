from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendWarnOnLevelGainStateMessage(INetworkMessage):
    protocolId = 7352
    enable:bool
    
    
