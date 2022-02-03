from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyMemberArenaInformations(PartyMemberInformations):
    rank:int
    

    def init(self, rank:int, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, initiative:int, alignmentSide:int, worldX:int, worldY:int, mapId:int, subAreaId:int, status:'PlayerStatus', entities:list['PartyEntityBaseInformation'], sex:bool, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.rank = rank
        
        super().__init__(lifePoints, maxLifePoints, prospecting, regenRate, initiative, alignmentSide, worldX, worldY, mapId, subAreaId, status, entities, sex, entityLook, breed, level, name, id)
    
    