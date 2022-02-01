from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayAggressionMessage(NetworkMessage):
    attackerId:int
    defenderId:int
    
    
