from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationOfferMessage(INetworkMessage):
    protocolId = 6717
    host:CharacterMinimalInformations
    timeLeftBeforeCancel:int
    
    
