from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightHumanReadyStateMessage(INetworkMessage):
    protocolId = 4318
    characterId:int
    isReady:bool
    
    
