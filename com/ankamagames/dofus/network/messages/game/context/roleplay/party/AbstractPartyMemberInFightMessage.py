from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    reason:int
    memberId:int
    memberAccountId:int
    memberName:str
    fightId:int
    timeBeforeFightStart:int
    
    
