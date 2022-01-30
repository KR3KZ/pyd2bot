from com.ankamagames.dofus.network.messages.game.social.ContactLookRequestMessage import ContactLookRequestMessage


class ContactLookRequestByIdMessage(ContactLookRequestMessage):
    protocolId = 7749
    playerId:int
    
