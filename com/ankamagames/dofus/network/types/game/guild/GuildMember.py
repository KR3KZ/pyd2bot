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
    sex:bool
    havenBagShared:bool
    

    def init(self, breed_:int, rank_:int, givenExperience_:int, experienceGivenPercent_:int, rights_:int, connected_:int, alignmentSide_:int, hoursSinceLastConnection_:int, moodSmileyId_:int, accountId_:int, achievementPoints_:int, status_:'PlayerStatus', sex_:bool, havenBagShared_:bool, level_:int, name_:str, id_:int):
        self.breed = breed_
        self.rank = rank_
        self.givenExperience = givenExperience_
        self.experienceGivenPercent = experienceGivenPercent_
        self.rights = rights_
        self.connected = connected_
        self.alignmentSide = alignmentSide_
        self.hoursSinceLastConnection = hoursSinceLastConnection_
        self.moodSmileyId = moodSmileyId_
        self.accountId = accountId_
        self.achievementPoints = achievementPoints_
        self.status = status_
        self.sex = sex_
        self.havenBagShared = havenBagShared_
        
        super().__init__(level_, name_, id_)
    
    