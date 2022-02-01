from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderPlayer(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    
    
