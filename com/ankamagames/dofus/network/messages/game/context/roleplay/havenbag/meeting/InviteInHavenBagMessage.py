from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagMessage(NetworkMessage):
    protocolId = 2929
    guestInformations:CharacterMinimalInformations
    accept:bool
    
    
