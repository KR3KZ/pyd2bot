from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


class PartyMemberInformations(CharacterBaseInformations):
    protocolId = 8492
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    initiative:int
    alignmentSide:int
    worldX:int
    worldY:int
    mapId:float
    subAreaId:int
    status:PlayerStatus
    entities:list[PartyEntityBaseInformation]
    
