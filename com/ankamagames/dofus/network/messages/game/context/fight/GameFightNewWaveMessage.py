from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightNewWaveMessage(INetworkMessage):
    protocolId = 1312
    id:int
    teamId:int
    nbTurnBeforeNextWave:int
    
    
