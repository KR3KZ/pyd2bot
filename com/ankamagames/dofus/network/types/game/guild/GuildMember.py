from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class GuildMember(CharacterMinimalInformations):
    protocolId = 5491
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
    status:PlayerStatus
    
