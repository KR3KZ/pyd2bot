from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    followedId:int
    success:bool
    isFollowed:bool
    
    
