from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.social.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


class AllianceInsiderInfoMessage(NetworkMessage):
    protocolId = 3553
    allianceInfos:AllianceFactSheetInformations
    guilds:list[GuildInsiderFactSheetInformations]
    prisms:list[PrismSubareaEmptyInfo]
    
