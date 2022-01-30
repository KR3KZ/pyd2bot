from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendSetWarnOnLevelGainMessage(NetworkMessage):
    protocolId = 4065
    enable:bool
    
