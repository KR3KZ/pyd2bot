from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FightStartingPositions(NetworkMessage):
    protocolId = 9707
    positionsForChallengers:int
    positionsForDefenders:int
    
    
