from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToGameServerMessage(NetworkMessage):
    validToken:bool
    ticket:list[int]
    homeServerId:int
    
    
