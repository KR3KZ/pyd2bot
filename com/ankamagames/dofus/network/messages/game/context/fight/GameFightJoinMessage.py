from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightJoinMessage(NetworkMessage):
    timeMaxBeforeFightStart:int
    fightType:int
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    
    
