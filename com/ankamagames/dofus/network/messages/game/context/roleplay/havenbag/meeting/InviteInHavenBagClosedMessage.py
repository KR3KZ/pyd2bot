from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagClosedMessage(INetworkMessage):
    protocolId = 5490
    hostInformations:CharacterMinimalInformations
    
    
