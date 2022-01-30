from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildApplicationListenMessage(NetworkMessage):
    protocolId = 9375
    listen:bool
    
