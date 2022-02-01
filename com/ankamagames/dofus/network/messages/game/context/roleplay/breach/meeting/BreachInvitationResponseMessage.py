from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachInvitationResponseMessage(INetworkMessage):
    protocolId = 6585
    guest:CharacterMinimalInformations
    accept:bool
    
    
