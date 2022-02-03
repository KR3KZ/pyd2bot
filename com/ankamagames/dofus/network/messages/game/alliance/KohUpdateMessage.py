from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
    


class KohUpdateMessage(NetworkMessage):
    alliances:list['AllianceInformations']
    allianceNbMembers:list[int]
    allianceRoundWeigth:list[int]
    allianceMatchScore:list[int]
    allianceMapWinners:list['BasicAllianceInformations']
    allianceMapWinnerScore:int
    allianceMapMyAllianceScore:int
    nextTickTime:int
    

    def init(self, alliances:list['AllianceInformations'], allianceNbMembers:list[int], allianceRoundWeigth:list[int], allianceMatchScore:list[int], allianceMapWinners:list['BasicAllianceInformations'], allianceMapWinnerScore:int, allianceMapMyAllianceScore:int, nextTickTime:int):
        self.alliances = alliances
        self.allianceNbMembers = allianceNbMembers
        self.allianceRoundWeigth = allianceRoundWeigth
        self.allianceMatchScore = allianceMatchScore
        self.allianceMapWinners = allianceMapWinners
        self.allianceMapWinnerScore = allianceMapWinnerScore
        self.allianceMapMyAllianceScore = allianceMapMyAllianceScore
        self.nextTickTime = nextTickTime
        
        super().__init__()
    
    