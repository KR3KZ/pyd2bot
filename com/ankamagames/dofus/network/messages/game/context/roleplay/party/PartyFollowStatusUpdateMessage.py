from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    protocolId = 4806
    followedId:int
    success:bool
    isFollowed:bool
    
    
