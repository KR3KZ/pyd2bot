from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationCloseMessage(INetworkMessage):
    protocolId = 3262
    host:CharacterMinimalInformations
    
    
