from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildMemberLeavingMessage(NetworkMessage):
    protocolId = 419
    kicked:bool
    memberId:int
    
    
