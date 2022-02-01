from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


class KohUpdateMessage(INetworkMessage):
    protocolId = 6530
    alliances:AllianceInformations
    allianceNbMembers:int
    allianceRoundWeigth:int
    allianceMatchScore:int
    allianceMapWinners:BasicAllianceInformations
    allianceMapWinnerScore:int
    allianceMapMyAllianceScore:int
    nextTickTime:int
    
    
