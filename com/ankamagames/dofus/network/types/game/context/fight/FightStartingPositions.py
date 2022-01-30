from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FightStartingPositions(INetworkMessage):
    protocolId = 9707
    positionsForChallengers:int
    positionsForDefenders:int
    
    
