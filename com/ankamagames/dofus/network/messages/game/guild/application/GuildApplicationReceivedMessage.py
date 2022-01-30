from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildApplicationReceivedMessage(INetworkMessage):
    protocolId = 3891
    playerName:str
    playerId:int
    
    
