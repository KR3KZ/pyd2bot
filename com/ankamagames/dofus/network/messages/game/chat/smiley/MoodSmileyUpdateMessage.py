from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MoodSmileyUpdateMessage(NetworkMessage):
    protocolId = 8249
    accountId:int
    playerId:int
    smileyId:int
    
    
