from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


@dataclass
class KohUpdateMessage(NetworkMessage):
    alliances:list[AllianceInformations]
    allianceNbMembers:list[int]
    allianceRoundWeigth:list[int]
    allianceMatchScore:list[int]
    allianceMapWinners:list[BasicAllianceInformations]
    allianceMapWinnerScore:int
    allianceMapMyAllianceScore:int
    nextTickTime:int
    
    
    def __post_init__(self):
        super().__init__()
    