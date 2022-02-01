from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightNewWaveMessage(NetworkMessage):
    id:int
    teamId:int
    nbTurnBeforeNextWave:int
    
    
