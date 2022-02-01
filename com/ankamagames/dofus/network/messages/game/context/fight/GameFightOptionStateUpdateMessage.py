from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightOptionStateUpdateMessage(NetworkMessage):
    fightId:int
    teamId:int
    option:int
    state:bool
    
    
