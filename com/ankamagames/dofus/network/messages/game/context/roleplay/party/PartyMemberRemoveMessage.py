from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyMemberRemoveMessage(AbstractPartyEventMessage):
    leavingPlayerId:int
    
    
