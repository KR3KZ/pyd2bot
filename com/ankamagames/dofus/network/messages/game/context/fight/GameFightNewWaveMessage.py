from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightNewWaveMessage(NetworkMessage):
    protocolId = 1312
    id:int
    teamId:int
    nbTurnBeforeNextWave:int
    
    
