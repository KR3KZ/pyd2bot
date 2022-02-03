from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
    floor:int
    room:int
    

    def init(self, floor:int, room:int, reason:int, memberId:int, memberAccountId:int, memberName:str, fightId:int, timeBeforeFightStart:int, partyId:int):
        self.floor = floor
        self.room = room
        
        super().__init__(reason, memberId, memberAccountId, memberName, fightId, timeBeforeFightStart, partyId)
    
    