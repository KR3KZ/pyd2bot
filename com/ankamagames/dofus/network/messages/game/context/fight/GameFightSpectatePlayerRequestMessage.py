from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightSpectatePlayerRequestMessage(NetworkMessage):
    protocolId = 9098
    playerId:int
    
