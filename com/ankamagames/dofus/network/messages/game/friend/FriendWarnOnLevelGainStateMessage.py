from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendWarnOnLevelGainStateMessage(NetworkMessage):
    protocolId = 7352
    enable:bool
    
    
