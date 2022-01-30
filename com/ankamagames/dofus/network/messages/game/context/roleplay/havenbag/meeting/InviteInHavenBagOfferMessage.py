from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagOfferMessage(NetworkMessage):
    protocolId = 2440
    hostInformations:CharacterMinimalInformations
    timeLeftBeforeCancel:int
    
