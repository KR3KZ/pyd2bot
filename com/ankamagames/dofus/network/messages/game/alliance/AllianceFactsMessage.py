from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInAllianceInformations import GuildInAllianceInformations


class AllianceFactsMessage(NetworkMessage):
    infos:AllianceFactSheetInformations
    guilds:list[GuildInAllianceInformations]
    controlledSubareaIds:list[int]
    leaderCharacterId:int
    leaderCharacterName:str
    
    
