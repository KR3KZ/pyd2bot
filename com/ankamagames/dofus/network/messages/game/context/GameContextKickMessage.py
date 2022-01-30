from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameContextKickMessage(INetworkMessage):
    protocolId = 2712
    targetId:int
    
    
