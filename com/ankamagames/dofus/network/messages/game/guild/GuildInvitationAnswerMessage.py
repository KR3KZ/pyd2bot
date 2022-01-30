from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationAnswerMessage(NetworkMessage):
    protocolId = 8895
    accept:bool
    
