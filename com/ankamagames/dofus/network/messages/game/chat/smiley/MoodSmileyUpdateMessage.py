from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MoodSmileyUpdateMessage(INetworkMessage):
    protocolId = 8249
    accountId:int
    playerId:int
    smileyId:int
    
    
