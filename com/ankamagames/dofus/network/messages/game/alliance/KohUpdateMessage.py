from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


class KohUpdateMessage(NetworkMessage):
    alliances:list[AllianceInformations]
    allianceNbMembers:list[int]
    allianceRoundWeigth:list[int]
    allianceMatchScore:list[int]
    allianceMapWinners:list[BasicAllianceInformations]
    allianceMapWinnerScore:int
    allianceMapMyAllianceScore:int
    nextTickTime:int
    
    
