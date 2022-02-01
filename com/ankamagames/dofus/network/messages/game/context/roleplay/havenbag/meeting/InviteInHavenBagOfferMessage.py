from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class InviteInHavenBagOfferMessage(INetworkMessage):
    protocolId = 2440
    hostInformations:CharacterMinimalInformations
    timeLeftBeforeCancel:int
    
    
