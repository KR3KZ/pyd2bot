from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachKickResponseMessage(NetworkMessage):
    protocolId = 5114
    target:CharacterMinimalInformations
    kicked:bool
    
    
