from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFighterStatusMessage(NetworkMessage):
    fightId:int
    playerId:int
    accepted:bool
    
    
