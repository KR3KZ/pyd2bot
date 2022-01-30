from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaFighterStatusMessage(NetworkMessage):
    protocolId = 5125
    fightId:int
    playerId:float
    accepted:bool
    
