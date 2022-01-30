from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class PartyInvitationRequestMessage(INetworkMessage):
    protocolId = 6419
    target:AbstractPlayerSearchInformation
    
    
