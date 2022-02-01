from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    registered:bool
    step:int
    battleMode:int
    
    
