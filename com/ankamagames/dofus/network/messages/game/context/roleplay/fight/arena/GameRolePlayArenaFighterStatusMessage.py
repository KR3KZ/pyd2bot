from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaFighterStatusMessage(INetworkMessage):
    protocolId = 5125
    fightId:int
    playerId:int
    accepted:bool
    
    
