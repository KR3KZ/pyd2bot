from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagClosedMessage(NetworkMessage):
    protocolId = 5490
    hostInformations:CharacterMinimalInformations
    
    
