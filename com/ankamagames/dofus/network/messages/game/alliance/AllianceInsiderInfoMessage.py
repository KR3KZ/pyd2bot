from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.social.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


class AllianceInsiderInfoMessage(INetworkMessage):
    protocolId = 3553
    allianceInfos:AllianceFactSheetInformations
    guilds:GuildInsiderFactSheetInformations
    prisms:PrismSubareaEmptyInfo
    
    
