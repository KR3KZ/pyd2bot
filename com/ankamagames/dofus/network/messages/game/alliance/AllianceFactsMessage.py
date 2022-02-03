from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInAllianceInformations import GuildInAllianceInformations
    


class AllianceFactsMessage(NetworkMessage):
    infos:'AllianceFactSheetInformations'
    guilds:list['GuildInAllianceInformations']
    controlledSubareaIds:list[int]
    leaderCharacterId:int
    leaderCharacterName:str
    

    def init(self, infos:'AllianceFactSheetInformations', guilds:list['GuildInAllianceInformations'], controlledSubareaIds:list[int], leaderCharacterId:int, leaderCharacterName:str):
        self.infos = infos
        self.guilds = guilds
        self.controlledSubareaIds = controlledSubareaIds
        self.leaderCharacterId = leaderCharacterId
        self.leaderCharacterName = leaderCharacterName
        
        super().__init__()
    
    