from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


@dataclass
class AllianceJoinedMessage(NetworkMessage):
    allianceInfo:AllianceInformations
    enabled:bool
    leadingGuildId:int
    
    
    def __post_init__(self):
        super().__init__()
    