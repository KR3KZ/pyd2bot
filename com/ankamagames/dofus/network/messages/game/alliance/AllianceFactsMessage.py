from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInAllianceInformations import GuildInAllianceInformations


class AllianceFactsMessage(INetworkMessage):
    protocolId = 6820
    infos:AllianceFactSheetInformations
    guilds:GuildInAllianceInformations
    controlledSubareaIds:int
    leaderCharacterId:int
    leaderCharacterName:str
    
    
