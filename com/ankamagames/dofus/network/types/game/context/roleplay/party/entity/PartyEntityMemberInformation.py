from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation


class PartyEntityMemberInformation(PartyEntityBaseInformation):
    protocolId = 2136
    initiative:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    
