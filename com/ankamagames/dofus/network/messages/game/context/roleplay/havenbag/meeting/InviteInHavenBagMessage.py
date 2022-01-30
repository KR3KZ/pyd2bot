from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagMessage(INetworkMessage):
    protocolId = 2929
    guestInformations:CharacterMinimalInformations
    accept:bool
    
    
