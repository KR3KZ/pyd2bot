from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyRequestedMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    
    
