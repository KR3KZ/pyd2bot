from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightTurnEndMessage(INetworkMessage):
    protocolId = 4443
    id:int
    
    
