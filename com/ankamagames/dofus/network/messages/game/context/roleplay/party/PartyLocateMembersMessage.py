from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberGeoPosition import PartyMemberGeoPosition


class PartyLocateMembersMessage(AbstractPartyMessage):
    geopositions:list[PartyMemberGeoPosition]
    
    
