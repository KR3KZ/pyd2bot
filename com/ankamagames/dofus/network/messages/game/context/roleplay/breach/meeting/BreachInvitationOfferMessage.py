from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationOfferMessage(NetworkMessage):
    protocolId = 6717
    host:CharacterMinimalInformations
    timeLeftBeforeCancel:int
    
    
