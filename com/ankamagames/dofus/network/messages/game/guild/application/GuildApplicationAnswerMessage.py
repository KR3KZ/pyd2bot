from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationAnswerMessage(NetworkMessage):
    accepted:bool
    playerId:int
    
    
