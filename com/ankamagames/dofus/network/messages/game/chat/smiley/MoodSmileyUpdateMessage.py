from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MoodSmileyUpdateMessage(NetworkMessage):
    accountId:int
    playerId:int
    smileyId:int
    
    
