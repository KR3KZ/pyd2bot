from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    protocolId = 1888
    reason:int
    memberId:int
    memberAccountId:int
    memberName:str
    fightId:int
    timeBeforeFightStart:int
    
