from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildApplicationReceivedMessage(INetworkMessage):
    protocolId = 3891
    playerName:str
    playerId:int
    
    
