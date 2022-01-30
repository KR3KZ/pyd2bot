from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class GuildInvitationSearchMessage(INetworkMessage):
    protocolId = 5666
    target:AbstractPlayerSearchInformation
    
    
