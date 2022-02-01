from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayFightRequestCanceledMessage(NetworkMessage):
    fightId:int
    sourceId:int
    targetId:int
    
    
