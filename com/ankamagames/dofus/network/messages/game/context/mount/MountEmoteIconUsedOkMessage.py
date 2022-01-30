from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountEmoteIconUsedOkMessage(INetworkMessage):
    protocolId = 1654
    mountId:int
    reactionType:int
    
    
