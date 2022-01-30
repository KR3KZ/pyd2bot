from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationCloseMessage(NetworkMessage):
    protocolId = 3262
    host:CharacterMinimalInformations
    
    
