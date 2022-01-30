from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationResponseMessage(NetworkMessage):
    protocolId = 6585
    guest:CharacterMinimalInformations
    accept:bool
    
