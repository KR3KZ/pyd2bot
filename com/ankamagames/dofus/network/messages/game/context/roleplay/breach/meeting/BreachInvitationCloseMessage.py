from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationCloseMessage(NetworkMessage):
    host:CharacterMinimalInformations
    
    
