from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateMapPlayersAgressableStatusMessage(NetworkMessage):
    playerIds:list[int]
    enable:list[int]
    
    
