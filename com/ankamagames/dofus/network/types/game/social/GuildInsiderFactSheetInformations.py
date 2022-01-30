from com.ankamagames.dofus.network.types.game.social.GuildFactSheetInformations import GuildFactSheetInformations


class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
    protocolId = 8132
    leaderName:str
    nbConnectedMembers:int
    nbTaxCollectors:int
    
    
