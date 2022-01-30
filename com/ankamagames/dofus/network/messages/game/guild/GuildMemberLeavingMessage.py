from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildMemberLeavingMessage(INetworkMessage):
    protocolId = 419
    kicked:bool
    memberId:int
    
    
