from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildInvitationMessage(INetworkMessage):
    protocolId = 2715
    targetId:int
    
    
