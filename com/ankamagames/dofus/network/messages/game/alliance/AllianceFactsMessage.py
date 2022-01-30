from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInAllianceInformations import GuildInAllianceInformations


class AllianceFactsMessage(NetworkMessage):
    protocolId = 6820
    infos:AllianceFactSheetInformations
    guilds:list[GuildInAllianceInformations]
    controlledSubareaIds:list[int]
    leaderCharacterId:float
    leaderCharacterName:str
    
