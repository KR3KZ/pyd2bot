from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildApplicationAnswerMessage(INetworkMessage):
    protocolId = 5404
    accepted:bool
    playerId:int
    
    
