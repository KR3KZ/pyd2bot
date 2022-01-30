from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightHumanReadyStateMessage(NetworkMessage):
    protocolId = 4318
    characterId:float
    isReady:bool
    
