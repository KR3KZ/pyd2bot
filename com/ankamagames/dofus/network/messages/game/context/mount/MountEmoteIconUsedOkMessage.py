from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountEmoteIconUsedOkMessage(NetworkMessage):
    protocolId = 1654
    mountId:int
    reactionType:int
    
