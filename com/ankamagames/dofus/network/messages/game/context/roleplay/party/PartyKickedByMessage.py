from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyKickedByMessage(AbstractPartyMessage):
    protocolId = 8439
    kickerId:int
    
    
