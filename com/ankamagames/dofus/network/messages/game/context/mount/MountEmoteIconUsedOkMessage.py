from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountEmoteIconUsedOkMessage(INetworkMessage):
    protocolId = 1654
    mountId:int
    reactionType:int
    
    
