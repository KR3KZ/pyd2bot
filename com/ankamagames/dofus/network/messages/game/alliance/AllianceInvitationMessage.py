from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceInvitationMessage(NetworkMessage):
    protocolId = 235
    targetId:int
    
    
