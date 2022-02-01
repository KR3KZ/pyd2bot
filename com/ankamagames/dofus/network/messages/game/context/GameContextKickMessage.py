from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameContextKickMessage(INetworkMessage):
    protocolId = 2712
    targetId:int
    
    
