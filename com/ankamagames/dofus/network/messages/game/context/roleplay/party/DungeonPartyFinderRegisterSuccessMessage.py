from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderRegisterSuccessMessage(NetworkMessage):
    dungeonIds:list[int]
    
    
