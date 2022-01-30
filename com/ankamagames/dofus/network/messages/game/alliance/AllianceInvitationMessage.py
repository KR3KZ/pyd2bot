from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceInvitationMessage(INetworkMessage):
    protocolId = 235
    targetId:int
    
    
