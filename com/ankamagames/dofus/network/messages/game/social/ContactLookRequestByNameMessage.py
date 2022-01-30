from com.ankamagames.dofus.network.messages.game.social.ContactLookRequestMessage import ContactLookRequestMessage


class ContactLookRequestByNameMessage(ContactLookRequestMessage):
    protocolId = 4808
    playerName:str
    
