from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightSpectatePlayerRequestMessage(INetworkMessage):
    protocolId = 9098
    playerId:int
    
    
