from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended


class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
    fightMap:MapCoordinatesExtended
    
    
