from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class PartyInvitationRequestMessage(NetworkMessage):
    protocolId = 6419
    target:AbstractPlayerSearchInformation
    
    
