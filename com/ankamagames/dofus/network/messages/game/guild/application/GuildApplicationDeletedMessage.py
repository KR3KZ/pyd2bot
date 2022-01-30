from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildApplicationDeletedMessage(NetworkMessage):
    protocolId = 5546
    deleted:bool
    
