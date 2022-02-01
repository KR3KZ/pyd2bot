from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MoodSmileyUpdateMessage(INetworkMessage):
    protocolId = 8249
    accountId:int
    playerId:int
    smileyId:int
    
    
