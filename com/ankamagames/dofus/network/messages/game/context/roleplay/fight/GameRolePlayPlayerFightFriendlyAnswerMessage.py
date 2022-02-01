from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnswerMessage(NetworkMessage):
    fightId:int
    accept:bool
    
    
