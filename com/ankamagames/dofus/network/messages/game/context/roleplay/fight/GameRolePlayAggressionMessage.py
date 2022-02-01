from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayAggressionMessage(INetworkMessage):
    protocolId = 2660
    attackerId:int
    defenderId:int
    
    
