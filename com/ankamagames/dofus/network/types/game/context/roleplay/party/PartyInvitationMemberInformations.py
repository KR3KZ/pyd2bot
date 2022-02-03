from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyInvitationMemberInformations(CharacterBaseInformations):
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    entities:list['PartyEntityBaseInformation']
    

    def init(self, worldX:int, worldY:int, mapId:int, subAreaId:int, entities:list['PartyEntityBaseInformation'], sex:bool, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.entities = entities
        
        super().__init__(sex, entityLook, breed, level, name, id)
    
    