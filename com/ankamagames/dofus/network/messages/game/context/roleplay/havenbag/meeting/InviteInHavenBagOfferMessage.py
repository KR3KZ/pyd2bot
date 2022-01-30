from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagOfferMessage(INetworkMessage):
    protocolId = 2440
    hostInformations:CharacterMinimalInformations
    timeLeftBeforeCancel:int
    
    
