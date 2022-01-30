from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightNewRoundMessage(INetworkMessage):
    protocolId = 1656
    roundNumber:int
    
    
