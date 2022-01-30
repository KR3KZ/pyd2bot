from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightJoinRequestMessage(NetworkMessage):
    protocolId = 6519
    fighterId:int
    fightId:int
    
