from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildApplicationAnswerMessage(INetworkMessage):
    protocolId = 5404
    accepted:bool
    playerId:int
    
    
