from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceGuildLeavingMessage(NetworkMessage):
    protocolId = 129
    kicked:bool
    guildId:int
    
