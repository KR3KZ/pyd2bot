from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightJoinMessage(INetworkMessage):
    protocolId = 1185
    timeMaxBeforeFightStart:int
    fightType:int
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    
    
