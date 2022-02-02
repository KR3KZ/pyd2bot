from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


@dataclass
class PartyInvitationRequestMessage(NetworkMessage):
    target:AbstractPlayerSearchInformation
    
    
    def __post_init__(self):
        super().__init__()
    