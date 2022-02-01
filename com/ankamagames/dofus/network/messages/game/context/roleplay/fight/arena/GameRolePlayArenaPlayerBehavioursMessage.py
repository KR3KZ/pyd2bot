from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaPlayerBehavioursMessage(NetworkMessage):
    flags:list[str]
    sanctions:list[str]
    banDuration:int
    
    
