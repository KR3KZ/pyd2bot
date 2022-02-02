from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


@dataclass
class PartyInvitationMemberInformations(CharacterBaseInformations):
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    entities:list[PartyEntityBaseInformation]
    
    
    def __post_init__(self):
        super().__init__()
    