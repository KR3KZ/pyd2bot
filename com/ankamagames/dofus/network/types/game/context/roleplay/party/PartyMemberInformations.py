from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


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
    status:'PlayerStatus'
    entities:list['PartyEntityBaseInformation']
    

    def init(self, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, initiative:int, alignmentSide:int, worldX:int, worldY:int, mapId:int, subAreaId:int, status:'PlayerStatus', entities:list['PartyEntityBaseInformation'], sex:bool, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.lifePoints = lifePoints
        self.maxLifePoints = maxLifePoints
        self.prospecting = prospecting
        self.regenRate = regenRate
        self.initiative = initiative
        self.alignmentSide = alignmentSide
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.status = status
        self.entities = entities
        
        super().__init__(sex, entityLook, breed, level, name, id)
    
    