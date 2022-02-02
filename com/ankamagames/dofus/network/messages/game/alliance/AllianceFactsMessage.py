from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInAllianceInformations import GuildInAllianceInformations


@dataclass
class AllianceFactsMessage(NetworkMessage):
    infos:AllianceFactSheetInformations
    guilds:list[GuildInAllianceInformations]
    controlledSubareaIds:list[int]
    leaderCharacterId:int
    leaderCharacterName:str
    
    
    def __post_init__(self):
        super().__init__()
    