from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildModificationStartedMessage(INetworkMessage):
    protocolId = 310
    canChangeName:bool
    canChangeEmblem:bool
    
    
