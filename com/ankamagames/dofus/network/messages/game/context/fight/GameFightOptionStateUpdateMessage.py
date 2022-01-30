from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightOptionStateUpdateMessage(NetworkMessage):
    protocolId = 4608
    fightId:int
    teamId:int
    option:int
    state:bool
    
