from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class GuildMember(CharacterMinimalInformations):
    breed:int
    rank:int
    givenExperience:int
    experienceGivenPercent:int
    rights:int
    connected:int
    alignmentSide:int
    hoursSinceLastConnection:int
    moodSmileyId:int
    accountId:int
    achievementPoints:int
    status:'PlayerStatus'
    sex:bool
    havenBagShared:bool
    

    def init(self, breed:int, rank:int, givenExperience:int, experienceGivenPercent:int, rights:int, connected:int, alignmentSide:int, hoursSinceLastConnection:int, moodSmileyId:int, accountId:int, achievementPoints:int, status:'PlayerStatus', level:int, name:str, id:int):
        self.breed = breed
        self.rank = rank
        self.givenExperience = givenExperience
        self.experienceGivenPercent = experienceGivenPercent
        self.rights = rights
        self.connected = connected
        self.alignmentSide = alignmentSide
        self.hoursSinceLastConnection = hoursSinceLastConnection
        self.moodSmileyId = moodSmileyId
        self.accountId = accountId
        self.achievementPoints = achievementPoints
        self.status = status
        
        super().__init__(level, name, id)
    
    