from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildApplicationReceivedMessage(NetworkMessage):
    protocolId = 3891
    playerName:str
    playerId:float
    
