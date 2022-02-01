from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(NetworkMessage):
    address:str
    ports:list[int]
    ticket:list[int]
    
    
