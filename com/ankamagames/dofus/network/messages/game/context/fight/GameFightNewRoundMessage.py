from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightNewRoundMessage(NetworkMessage):
    protocolId = 1656
    roundNumber:int
    
    
