from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
    


class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
    fightMap:'MapCoordinatesExtended'
    

    def init(self, fightMap:'MapCoordinatesExtended', reason:int, memberId:int, memberAccountId:int, memberName:str, fightId:int, timeBeforeFightStart:int, partyId:int):
        self.fightMap = fightMap
        
        super().__init__(reason, memberId, memberAccountId, memberName, fightId, timeBeforeFightStart, partyId)
    
    