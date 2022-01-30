from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightJoinRequestMessage(INetworkMessage):
    protocolId = 6519
    fighterId:int
    fightId:int
    
    
