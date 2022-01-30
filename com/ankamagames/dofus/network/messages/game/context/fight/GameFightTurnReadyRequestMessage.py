from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightTurnReadyRequestMessage(INetworkMessage):
    protocolId = 4389
    id:int
    
    
