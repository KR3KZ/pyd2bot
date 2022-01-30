from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightJoinMessage(INetworkMessage):
    protocolId = 1185
    timeMaxBeforeFightStart:int
    fightType:int
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    
    
