from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    accept:bool
    
    
