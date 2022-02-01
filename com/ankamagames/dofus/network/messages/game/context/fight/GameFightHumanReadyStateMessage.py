from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightHumanReadyStateMessage(INetworkMessage):
    protocolId = 4318
    characterId:int
    isReady:bool
    
    
