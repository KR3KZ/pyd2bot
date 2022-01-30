from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildApplicationAnswerMessage(NetworkMessage):
    protocolId = 5404
    accepted:bool
    playerId:int
    
