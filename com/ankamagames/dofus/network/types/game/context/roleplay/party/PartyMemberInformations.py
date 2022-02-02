from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


@dataclass
class PartyMemberInformations(CharacterBaseInformations):
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    initiative:int
    alignmentSide:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    status:PlayerStatus
    entities:list[PartyEntityBaseInformation]
    
    
    def __post_init__(self):
        super().__init__()
    