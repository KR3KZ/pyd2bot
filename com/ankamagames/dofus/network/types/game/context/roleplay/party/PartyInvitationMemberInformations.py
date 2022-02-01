from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


class PartyInvitationMemberInformations(CharacterBaseInformations):
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    entities:list[PartyEntityBaseInformation]
    
    
