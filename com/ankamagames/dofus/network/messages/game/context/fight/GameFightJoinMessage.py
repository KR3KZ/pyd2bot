from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightJoinMessage(NetworkMessage):
    protocolId = 1185
    timeMaxBeforeFightStart:int
    fightType:int
    isTeamPhase:bool
    canBeCancelled:bool
    canSayReady:bool
    isFightStarted:bool
    
    
