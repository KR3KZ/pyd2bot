from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class UpdateMapPlayersAgressableStatusMessage(INetworkMessage):
    protocolId = 3658
    playerIds:int
    enable:int
    
    
