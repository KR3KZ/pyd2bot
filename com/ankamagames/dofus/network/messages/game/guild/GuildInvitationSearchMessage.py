from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class GuildInvitationSearchMessage(NetworkMessage):
    protocolId = 5666
    target:AbstractPlayerSearchInformation
    
