from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationMessage(NetworkMessage):
    protocolId = 2715
    targetId:float
    
