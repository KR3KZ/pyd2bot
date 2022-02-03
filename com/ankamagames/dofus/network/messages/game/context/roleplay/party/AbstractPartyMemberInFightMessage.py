from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    reason:int
    memberId:int
    memberAccountId:int
    memberName:str
    fightId:int
    timeBeforeFightStart:int
    

    def init(self, reason:int, memberId:int, memberAccountId:int, memberName:str, fightId:int, timeBeforeFightStart:int, partyId:int):
        self.reason = reason
        self.memberId = memberId
        self.memberAccountId = memberAccountId
        self.memberName = memberName
        self.fightId = fightId
        self.timeBeforeFightStart = timeBeforeFightStart
        
        super().__init__(partyId)
    
    